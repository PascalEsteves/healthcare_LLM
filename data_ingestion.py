from datasets import load_dataset
import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
from database import CLIENT_QD

def split_text(full_string):
    split_string = full_string.split('### ')
    input_string = ""
    answer_string = ""

    if len(split_string[1])>1000:
        input_string = split_string[1][:500] +'\n'+ split_string[1][500:]
    else:
        input_string = split_string[1]

    if len(split_string[2])>1000:
        answer_string = split_string[2][:500] +'\n'+ split_string[2][500:]
    else:
        answer_string = split_string[2]
    text = input_string + '\n' + answer_string

    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    return chunks

def main():
    cl = CLIENT_QD()
    data = load_dataset("taaredikahan23/Medical_dataset",split='train')
    df = data.to_pandas()
    aux_text = ""
    for _, row in df.iterrows():
        aux_text+= split_text(str(row['text']))+"\n"
    text= get_text_chunks(aux_text)

    cl.add_data_storate(text)

if __name__ == '__main__':
    main()