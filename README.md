# LLM + Langchain + Qdrant Cloud - RAG
## Features
- UI developed with streamlit for easy interaction with solution 
- Application of RAG architecture with LLM : meta-llama/Llama-2-7b-chat-hf , encoding model :BAAI/bge-large-en-v1.5
- Integration with Qdrant's Managed Cloud Service
- Suplied dataset : taaredikahan23/Medical_dataset , source: https://huggingface.co/datasets](https://huggingface.co/datasets/taaredikahan23/Medical_dataset

## Installation:
# Step 1 - Clone this repository to your local machine:
```sh
git clone https://github.com/PascalEsteves/healthcare_LLM.git
```
# Step 2  - Create virtual env
go to the cloned repository directory
```sh
python -m venv .
```
# Step 3  - Activate env
MAC:
```sh
source bin/activate
```
Windows:
```sh
Scripts\activate
```
# Step 4 - Install Requirements
```sh
pip install -r requirements.tx
```
# Step 5 - Creat .env file
Create .env file in a text editor and provide your Qdrant Managed Cloud Service creadentials and huggingface api token

# Step 6  - Start app
```sh
streamlit run app.py
```
# Autor
Pascal Esteves

