# Simple-Langchain-Chat
How to use LangChain and OpenAI's GPT models to create a translation service

## Features
- Language translation between English and other languages (e.g., Spanish, Turkish).
- Simple prompt-based interaction using OpenAI GPT models.
- FastAPI integration for serving the translation chain via an HTTP API.
- Modular scripts demonstrating both CLI and API-based translation.
- Utilizes LangChain’s prompt chaining and output parsing utilities.

## Files
- **simplemessage.py**: Basic example that sends a hardcoded prompt to OpenAI and prints the translation.
- **langchain_chain.py**: Uses LangChain’s `ChatPromptTemplate` and `StrOutputParser` for flexible text translation with language selection.
- **langchain_fastapi.py**: FastAPI app setup to expose the LangChain translation chain via an endpoint.
- **langchain_with_fastapi.py**: Full integration of LangChain prompt chaining and FastAPI routing using `langserve`.

## You can test API on
- [http://localhost:8000/chain/playground](http://localhost:8000/chain/playground)
- ![images](images/playground.png)



