from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
import qdrant_client
import os
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from database import CLIENT_QD

def get_llm():
    return HuggingFaceHub(repo_id="meta-llama/Llama-2-7b-chat-hf",
                          model_kwargs={"temperature":0.5, "max_new_tokens":512})

def handle_user(user_question, rag_pipeline):

    st.write(user_template.replace(
                "{{MSG}}", user_question), unsafe_allow_html=True)

    answer = rag_pipeline.run(user_question)

    st.write(bot_template.replace(
                "{{MSG}}", answer), unsafe_allow_html=True)

def main():

    load_dotenv()
    st.set_page_config(page_title="Chat with your Healthcare Solution",
                       page_icon=":doctor:")

    st.write(css, unsafe_allow_html=True)

    #get vector store
    CL_QD= CLIENT_QD()
    vector_store = CL_QD.vector_storage

    # create rag_pipeline
    rag_pipeline = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )

    st.header("Chat with your personal Doctor")
    user_question = st.text_input("Ask a question :")

    if user_question:
        handle_user(user_question,rag_pipeline)


if __name__ =='__main__':
    main()



