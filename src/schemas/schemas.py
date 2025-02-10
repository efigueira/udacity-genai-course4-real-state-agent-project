from typing import List
from pydantic import BaseModel, Field
import pandas as pd

from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from fastapi.encoders import jsonable_encoder


class PropertyDetails(BaseModel):
    neighborhood: str = Field(description="The specific area or district where the property is located")
    price: int = Field(description="The cost of the property in US dollars")
    bedrooms: int = Field(description="The total number of bedrooms")
    bathrooms: int = Field(description="The total number of bathrooms")
    house_size: int = Field(description="The total living area of the property measured in square feet")
    description: str = Field(description="A detailed overview of the property, including its features and appeal")
    neighborhood_description: str = Field(description="An overview of the surrounding area, including nearby amenities and community features")


class ListPropertyDetails(BaseModel):
    properties_list: List[PropertyDetails] = Field(description="A list of real estate properties")


def print_schemas(schema):
    text_list = []
    for key, value in schema.model_dump().items():
        text_list.append(f"{key}: {value}")
    text = '\n'.join(text_list)
    print(text)
    return text


class CreateRealEstateListingsPrompt:
    _instructions = ("Create a JSON object containing a minimum of 10 real "
                     "estate listings. Each listing should adhere to the "
                     "provided example schema for structure and formatting.")

    def __init__(self):
        self._parser = PydanticOutputParser(pydantic_object=ListPropertyDetails)

        self._prompt_template = PromptTemplate(
            template="{instructions}"
                     "\nListing example schema:"
                     "\n{property_example_text}"
                     "\n{parser_instructions}\n",
            input_variables=["instructions", "property_example_text"],
            partial_variables={
                "parser_instructions": self._parser.get_format_instructions()},
        )
        self._query = None
        self._response = None
        self._response_df = None

    def prepare_query(self, property_example_text: str):
        self._query = self._prompt_template.format(
            instructions=self._instructions,
            property_example_text=property_example_text,
        )
        return self._query

    def parse_response(self, response):
        self._response = self._parser.parse(response.content)
        return self._response

    def convert_response_to_df(self, response):
        parsed_response = self.parse_response(response)
        self._response_df = pd.DataFrame(jsonable_encoder(parsed_response.properties_list))
        return self._response_df