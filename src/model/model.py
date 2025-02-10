from langchain_openai import ChatOpenAI


class Model:
    def __init__(self, temperature: float = 0.5, model_name: str = "gpt-3.5-turbo", model: ChatOpenAI = ChatOpenAI):
        self._temperature = temperature
        self._model_name = model_name

        self._llm = model(model_name=model_name, temperature=temperature)

    @property
    def llm(self):
        return self._llm


