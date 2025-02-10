from langchain_openai import ChatOpenAI
from pathlib import Path
from diffusers import DiffusionPipeline


class Model:
    def __init__(self, temperature: float = 0.5, model_name: str = "gpt-3.5-turbo", model: ChatOpenAI = ChatOpenAI):
        self._temperature = temperature
        self._model_name = model_name

        self._llm = model(model_name=model_name, temperature=temperature)

    @property
    def llm(self):
        return self._llm


class ImageGenerator:
    _output_path = Path(__file__).parent.parent.parent / "images"
    _max_tokens = 77

    def __init__(self, img_description: str, img_name: str):
        self._output_path.mkdir(exist_ok=True, parents=True)
        self._img_description = img_description
        self._img_output_path = self._output_path / img_name

    def generate(self):
        pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipe = pipe.to("cpu")
        image = pipe(self._img_description).images[0]
        image.save(self._img_output_path)
        return self._img_output_path

    @property
    def img_path(self):
        return self._img_output_path
