import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import FastEmbedEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
load_dotenv()

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
def initialize_rag_pipeline(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_text(text)
    embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    db = FAISS.from_texts(texts, embeddings)
    retriever = db.as_retriever(search_type="similarity",kwargs={"k":4})
    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(model_name='llama3-70b-8192')
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=False)
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever,memory=memory)
    return chain

# Streamlit app
st.title("PDF Q&A Chatbot with RAG")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.info("Processing the uploaded PDF...")
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.info("Setting up the chatbot...")
    chatbot = initialize_rag_pipeline(pdf_text)
    st.success("Chatbot is ready! Start asking questions about your document.")

    if "history" not in st.session_state:
        st.session_state.history = []

    user_question = st.text_input("Ask a question:", key="user_input")

    if user_question:
        response = chatbot({"question": user_question, "chat_history": st.session_state.history})
        st.session_state.history.append((user_question, response['answer']))
        for question, answer in st.session_state.history:
            st.write(f"**You**: {question}")
            st.write(f"**Bot**: {answer}")
