from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (ensure you have an API key set)
load_dotenv()

# Initialize the OpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)


# Define the conversation messages
messages = [
    SystemMessage(content="Translate the following from English to Turkish:"),
    HumanMessage(content="What is Python?")
]

parser = StrOutputParser()
chain = model | parser #langchain


if __name__ == "__main__":

    # Print the response content
    print(parser.invoke(chain.invoke(messages)))

