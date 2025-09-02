**RAG using Langchain**


This project is a Retrieval-Augmented Generation (RAG) system that lets you query over PDF documents and website content using semantic search powered by embeddings. The system is built with:

LangChain for chaining document loaders, embeddings, and vector stores

ChromaDB as a persistent vector database

FastAPI to serve a RESTful API for querying

Postman or any client to test the API

**Features**

---- Load and split PDFs using PyPDFLoader

---- Extract data from websites

---- Embed documents using all-MiniLM-L6-v2 via HuggingFaceEmbeddings

---- Store and search embeddings using ChromaDB

---- Query via a FastAPI endpoint

---- Clean and modular code (RAG logic separated from API)
