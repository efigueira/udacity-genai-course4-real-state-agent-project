import pandas as pd
import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import matplotlib.pyplot as plt
import os
from PIL import Image
import uuid


from src.schemas import df_to_property_details, print_schemas


class RAGWithChromaClipEmbeddings:
    _db_name = 'real_state.db'
    _collection_name = "real_state_collection"
    _drop_cols = ["image_path"]

    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()
        self._client = chromadb.PersistentClient(path=self._db_name)

        existing_cols = self._client.list_collections()
        if self._collection_name in existing_cols:
            print(f"✅ Collection '{self._collection_name}' already exists. "
                  f"Skipping creation.")
            self._collection = self._client.get_or_create_collection(
                self._collection_name,
                embedding_function=OpenCLIPEmbeddingFunction(),
                data_loader=ImageLoader()
            )
        else:
            print(f"🆕 Creating new collection '{self._collection_name}'...")
            self._collection = self._client.get_or_create_collection(
                self._collection_name,
                embedding_function=OpenCLIPEmbeddingFunction(),
                data_loader=ImageLoader()
            )
            self._process()

    @staticmethod
    def _generate_uuid_from_text(text, namespace=uuid.NAMESPACE_DNS):
        return str(uuid.uuid5(namespace, text))

    def _process(self):
        self._df['complete_description'] = self._combine_text_columns()
        self._df['uuid'] = self._df.complete_description.apply(self._generate_uuid_from_text)
        existing_ids = set(self._collection.get()["ids"])
        filtered_df = self._df[~self._df['uuid'].isin(existing_ids)]

        if filtered_df.empty:
            print("✅ All descriptions already exist in the collection. Skipping processing.")
            return 0
        else:
            print(f"🔍 Processing {len(filtered_df)} new descriptions...")
            desc = filtered_df.complete_description.to_list()
            images = filtered_df.image_path.to_list()
            self._collection.add(ids=desc, uris=images)

    def _combine_text_columns(self):
        properties_schema = df_to_property_details(self._df)
        text = [print_schemas(prop) for prop in properties_schema]
        return text

    def query_db(self, query, results: int = 3):
        results = self._collection.query(
            query_texts=[query],
            n_results=results,
            include=["uris", "distances"]
        )
        return results

    @staticmethod
    def _show_image(image_path):
        if os.path.exists(image_path):
            image = Image.open(image_path)
            plt.figure(figsize=(5, 5))
            plt.imshow(image)
            plt.axis("off")
            # plt.title(f"Result {idx+1}")
            plt.show()
        else:
            print(f"⚠️ Image not found: {image_path}")

    def display_search_results(self, results):
        ids = results.get("ids", [[]])[0]  # Extracts first list (if multiple results exist)
        uris = results.get("uris", [[]])[0]  # Extracts first list (image paths)
        distances = results.get("distances", [[]])[0]  # Extract distances if available

        # No results
        if not ids or not uris:
            print("No results found.")
            return 0
        else:
            for idx, (text, image_path, distance) in enumerate(zip(ids, uris, distances)):
                text = '\n'.join(["\n" + "="*50,
                                  f"🏡 {idx+1}. House Suggestion (Distance: {distance:.4f})",
                                  text])
                print(text)
                self._show_image(image_path)
