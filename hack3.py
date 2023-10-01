import os
import json
from dotenv import load_dotenv
load_dotenv()
from typing import Any
from typing import List
from typing import Dict
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import pinecone
import tiktoken
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment="gcp-starter")
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

import pinecone

def run_llm(query:str) -> Any:
    embeddings=OpenAIEmbeddings()
    docsearch=Pinecone.from_existing_index(index_name="movewors-hackathon-one", embedding=embeddings)
    chat=ChatOpenAI(verbose=False, temperature=0)
    qa=RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=docsearch.as_retriever())
    #question_generator_chain = LLMChain(llm=chat)
    
    #qa=ConversationalRetrievalChain(llm=chat, retriever=docsearch.as_retriever())
    #qa=ConversationalRetrievalCha
    # in(retriever=docsearch.as_retriever(), output_key = 'answer', question_generator=question_generator_chain, combine_docs_chain=docsearch)
    
    return qa({"query":query})

if __name__=="__main__":
    print("hi")
    #print(run_llm(query="Who started Moveworks?"))

