from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


# Load environment variables (ensure you have an API key set)
load_dotenv()

# Initialize the OpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)


# Define the conversation messages
messages = [
    SystemMessage(content="Translate the following from English to Turkish:"),
    HumanMessage(content="What is Python?")
]

if __name__ == "__main__":

    # Invoke the model
    response = model.invoke(messages)

    # Print the response content
    print(response.content)

