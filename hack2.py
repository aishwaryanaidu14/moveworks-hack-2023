import os
import json
from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
import pinecone
import tiktoken
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment="gcp-starter")
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import Pinecone
import pinecone


if __name__ == "__main__":
    print("Hello LangChain!")
    loader = CSVLoader(file_path="C:/Users/Aishwarya/Documents/newdocs/langchain/ice_breaker/processed/scraped.csv", encoding='utf8')
    data = loader.load()
    print(len(data))
    textsplitter=RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
    docs=textsplitter.split_documents(documents=data)
    print(len(docs))
    
    embeddings=OpenAIEmbeddings()
    Pinecone.from_documents(docs, embeddings, index_name="movewors-hackathon-one")
    
    #loader = DirectoryLoader('C:/Users/Aishwarya/Documents/newdocs/langchain/ice_breaker/text', glob="**/*.txt")
   # loader = DirectoryLoader('C:/Users/Aishwarya/Documents/newdocs/langchain/ice_breaker/text', glob="**/*.txt", loader_cls=TextLoader)
   # docs=loader.load()
   # print(len(docs))
   #"Use the following pieces of context to answer the question at the end. If you do not know the answer, say you do not know. Do not try to make up an answer."
    
    

    

    

 