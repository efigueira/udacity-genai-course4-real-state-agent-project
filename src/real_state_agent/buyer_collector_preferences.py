from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


class BuyerCollectorPreferences:
    _questions = [
        "How big do you want your house to be?",
        "What are the 3 most important things for you in choosing a property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?",
    ]
    _answers = [
        "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
        "A quiet neighborhood, good local schools, and convenient shopping options.",
        "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
        "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
        "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
    ]
    def __init__(self, llm):
        self.llm = llm
        # Memory to remember the conversation
        self.memory = ConversationBufferMemory()
        # Conversation chain
        self.conversation_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory
        )
        self._preferences = None
        self._summary = None

    def collect(self):
        self._preferences = self._collect_preferences()
        self._summary = self._summarize_preferences()
        return self._summary

    def _collect_preferences(self):
        preferences = {}

        setup_message = f"""
        Assistant: You are going to ask the user a list of questions ({len(self._questions)} in total) about their property preferences, one by one. 
        After each question, listen carefully to the user's response and acknowledge it.
        Your role is to collect the preferences clearly and concisely.
        """

        print("LLM Setup: Setting the context for the assistant.")
        self.conversation_chain.run(setup_message.strip())

        for question, answer in zip(self._questions, self._answers):
            conversation_input = f"""
            Assistant: {question}
            User: {answer}
            """
            print(f"LLM (Question): {question}")
            print(f"User (Answer): {answer}")
            # Run the conversation with explicit roles
            response = self.conversation_chain.run(conversation_input.strip())
            preferences[question] = answer
            print(f"LLM (Response): {response.strip()}\n")
        return preferences

    def _summarize_preferences(self):
        # Format preferences into a single prompt for summarization
        preferences_text = "\n".join \
            ([f"{key}: {value}" for key, value in self._preferences.items()])

        prompt_template = """
        Using the buyer preferences provided below, create a concise summary of what the buyer is looking for in a property. 
        
        If the preferences include details such as the name of the neighborhood, the price, the number of bedrooms, the number of bathrooms, or the house size, include this information numerically wherever possible. Do not invent information. If the information is not provided, insert blank space. Format the summary according to the following schema:
        
        neighborhood: [Name of the neighborhood selected by the buyer]
        price: [Price in dollars]
        bedrooms: [Number of bedrooms]
        bathrooms: [Number of bathrooms]
        house_size: [House size in square feet]
        description: [A concise summary of the buyer’s requirements]
        
        Buyer Preferences:
        {preferences}
        """
        prompt = PromptTemplate(
            input_variables=["preferences"],
            template=prompt_template.strip()
        )

        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run({"preferences": preferences_text})

    @property
    def preferences(self):
        return self._preferences

    @property
    def summary(self):
        return self._summary
