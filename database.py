import qdrant_client
import os
from dotenv import load_dotenv
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings

class CLIENT_QD():

    def __init__(self):

        load_dotenv()
        self.host = os.getenv('QDRANT_HOST')
        self.api_key = os.getenv('QDRANT_API')
        self.collection_name = os.getenv('COLLECTION_NAME')
        self.embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5",
                                                model_kwargs={'device':"cpu"},
                                                encode_kwargs = {'normalize_embeddings': True})
        self.client = qdrant_client.QdrantClient(self.host, api_key=self.api_key)
        self.vector_config = qdrant_client.http.models.VectorParams(size=1024, # 1024 for BAAI/bge-large-en-v1.5
                                                                    distance=qdrant_client.http.models.Distance.COSINE)
        self.vector_storage = Qdrant(client=self.client,
                                    collection_name=self.collection_name,
                                    embeddings=self.embeddings)

    def create_collection(self, collection_name:str):

        return self.client.recreate_collection(
                collection_name=f"{collection_name}",
                vectors_config=self.vector_config)

    def add_data_storate(self,text:str):
        return self.vector_storage.add_texts(text)