from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

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

app = FastAPI(
    title="Translated Chat BOT",
    version="1.0.0",
    description="Translated Chat BOT"
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost", port=8000)
    # Print the response content
    print(parser.invoke(chain.invoke({"language" : "Spanish", "text" : "Hello World"})))

