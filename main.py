import os
import pinecone
from datasets import load_dataset   
from pinecone_text.sparse import BM25Encoder
from sentence_transformers import SentenceTransformer
import torch

# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = os.getenv("PINECONE_API_KEY") 
# find your environment next to the api key in pinecone console
env = os.getenv("PINECONE_ENVIRONMENT") 

# init connection to pinecone
pinecone.init(
    api_key=api_key,
    environment=env
)

def create_embeddings(name = "flipkart"):
    index_name = name 

    if index_name not in pinecone.list_indexes():
        # create the index
        pinecone.create_index(
        index_name,
        dimension=512,
        metric="dotproduct",
        pod_type="s1"
        )
    index = pinecone.Index(index_name)
    return index

def load_fashion_dataset():
    fashion = load_dataset(
    "ashraq/fashion-product-images-small",
    split="train"
    )
    return fashion

def create_images_and_metadata(fashion = load_fashion_dataset()):
    images = fashion["image"]
    metadata = fashion.remove_columns("image")
    return [images, metadata]

def create_sparse_embeddings(data = create_images_and_metadata()):
    bm25 = BM25Encoder()
    bm25.fit(data[1]['productDisplayName'])

def load_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = SentenceTransformer(
        'sentence-transformers/clip-ViT-B-32',
        device=device
    )
    return model



