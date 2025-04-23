from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (ensure you have an API key set)
load_dotenv()

# Initialize the OpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)


# Define the conversation messages
#messages = [
#    SystemMessage(content="Translate the following from English to Turkish:"),
#    HumanMessage(content="What is Python?")
#]

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser #langchain


if __name__ == "__main__":

    # Print the response content
    print(parser.invoke(chain.invoke({"language" : "Spanish", "text" : "Hello World"})))

