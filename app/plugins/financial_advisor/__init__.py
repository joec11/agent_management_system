import os
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.commands import Command

class FinancialAdvisorChat(Command):
    def __init__(self):
        super().__init__()
        self.name = "financial_advisor"
        self.description = "This agent provides personalized financial advice, offering tailored investment portfolio strategies based on risk tolerance, financial goals, and time horizon. Powered by AI, it analyzes market trends, historical performance, and potential risks to optimize returns while managing volatility."
        self.history = []
        load_dotenv()
        API_KEY = os.getenv('OPEN_AI_KEY')
        # you can try GPT4 but it costs a lot more money than the default 3.5
        self.llm = ChatOpenAI(openai_api_key=API_KEY, model="gpt-4-0125-preview")  # Initialize once and reuse
        # This is default 3.5 chatGPT
        # self.llm = ChatOpenAI(openai_api_key=API_KEY)  # Initialize once and reuse

    def calculate_tokens(self, text):
        # More accurate token calculation mimicking OpenAI's approach
        return len(text)

    def interact_with_ai(self, user_input, character_name):
        # Generate a more conversational and focused prompt
        prompt_text = "Design an investment portfolio strategy tailored to a client's risk tolerance, financial goals, and time horizon. Provide detailed recommendations on asset allocation, diversification, and specific investment vehicles across various markets (stocks, bonds, real estate, etc.). Consider factors such as historical performance, market trends, and potential risks to maximize returns while minimizing volatility."
        prompt = ChatPromptTemplate.from_messages(self.history + [("system", prompt_text)])

        output_parser = StrOutputParser()
        chain = prompt | self.llm | output_parser

        response = chain.invoke({"input": user_input})

        # Token usage logging and adjustment for more accurate counting
        tokens_used = self.calculate_tokens(prompt_text + user_input + response)
        logging.info(f"OpenAI API call made. Tokens used: {tokens_used}")
        return response, tokens_used

    def execute(self, *args, **kwargs):
        character_name = kwargs.get("character_name", "Financial Advisor")
        print(f"This is your Financial Advisor. What can I help you with?")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "done":
                print("Thank you for using the Financial Advisor Chat. Goodbye!")
                break

            self.history.append(("user", user_input))
  
            try:
                response, tokens_used = self.interact_with_ai(user_input, character_name)
                print(f"Financial Advisor: {response}")
                print(f"(This interaction used {tokens_used} tokens.)")
                self.history.append(("system", response))
            except Exception as e:
                print("Sorry, there was an error processing your request. Please try again.")
                logging.error(f"Error during interaction: {e}")
