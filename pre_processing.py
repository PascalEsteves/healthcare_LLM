import pandas as pd
import os
from PyPDF2 import PdfReader

def check_excel(doc):
    return doc.name.endswith(('.xlsx','.xls'))

def check_csv(doc):
    return doc.name.endswith('.csv')

def check_pdf(doc):
    return doc.name.endswith('.pdf')

def get_chunks_from_excel(doc):
    df = pd.read_excel(doc)
    text=""
    for _, row in df.iterrows:
        text+=str(row)
    return text

def get_chunks_from_csv(doc):
    df = pd.read_csv(doc)
    text=""
    for _, row in df.iterrows:
        text+=str(row)
    return text

def get_chunks_from_pdf(doc):
    pdf_reader = PdfReader(doc)
    text = ""
    for page in pdf_reader.pages:
        text +=page.extract_text()
    return text

def get_chunks_from_doc(docs):

    text = ""
    for doc in docs:
        if check_excel(doc):
            text+=get_chunks_from_excel(doc)
        elif check_csv(doc):
            text+=get_chunks_from_csv(doc)
        elif check_pdf(doc):
            text+=get_chunks_from_csv(doc)
        else:
            print('The ingetested format is not accepatable')

