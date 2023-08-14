import os
import pinecone
from datasets import load_dataset   
from pinecone_text.sparse import BM25Encoder
from sentence_transformers import SentenceTransformer
import torch
from tqdm.auto import tqdm
import pandas as pd
import pickle 
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = os.environ.get("PINECONE_API_KEY")
# find your environment next to the api key in pinecone console
env = os.environ.get("PINECONE_ENVIRONMENT") 

# init connection to pinecone
pinecone.init(
    api_key=api_key,
    environment=env
)


index_name = "flipkart"
if index_name not in pinecone.list_indexes():
    # create the index
    pinecone.create_index(
    index_name,
    dimension=512,
    metric="dotproduct",
    pod_type="s1"
    )
index = pinecone.Index(index_name)


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
    with open('bm25_encoder.pkl', 'wb') as f:
        pickle.dump(bm25, f)
    return bm25

def load_sparse_embeddings():
    with open('bm25_encoder.pkl', 'rb') as f:
        loaded_bm25 = pickle.load(f)
    return loaded_bm25

def load_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = SentenceTransformer(
        'sentence-transformers/clip-ViT-B-32',
        device=device
    )
    return model

def upsert_documents(fashion = load_fashion_dataset(), images = create_images_and_metadata()[0], metadata = create_images_and_metadata()[1], model = load_model(), bm25 = load_sparse_embeddings(), index = index):
    batch_size = 200
    for i in tqdm(range(0, len(fashion), batch_size)):
        # find end of batch
        i_end = min(i+batch_size, len(fashion))
        # extract metadata batch
        metadata = pd.DataFrame(metadata)
        meta_batch = metadata.iloc[i:i_end]
        meta_dict = meta_batch.to_dict(orient="records")
        # concatinate all metadata field except for id and year to form a single string
        meta_batch = [" ".join(x) for x in meta_batch.loc[:, ~meta_batch.columns.isin(['id', 'year'])].values.tolist()]
        # extract image batch
        img_batch = images[i:i_end]
        # create sparse BM25 vectors
        sparse_embeds = bm25.encode_documents([text for text in meta_batch])
        # create dense vectors
        dense_embeds = model.encode(img_batch).tolist()
        # create unique IDs
        ids = [str(x) for x in range(i, i_end)]

        upserts = []
        # loop through the data and create dictionaries for uploading documents to pinecone index
        for _id, sparse, dense, meta in zip(ids, sparse_embeds, dense_embeds, meta_dict):
            upserts.append({
                'id': _id,
                'sparse_values': sparse,
                'values': dense,
                'metadata': meta
            })
        # upload the documents to the new hybrid index
        index.upsert(upserts)
    # show index description after uploading the documents
    return index.describe_index_stats()

def make_query(query, model = load_model(), bm25 = load_sparse_embeddings(), index = index, images = create_images_and_metadata()[0]):
    query = query

    # create sparse and dense vectors
    sparse = bm25.encode_queries(query)
    dense = model.encode(query).tolist()
    # search
    result = index.query(
        top_k=14,
        vector=dense,
        sparse_vector=sparse,
        include_metadata=True
    )
    # used returned product ids to get images
    imgs = [images[int(r["id"])] for r in result["matches"]]
    return imgs

def hybrid_scale(dense, sparse, alpha: float):
    """Hybrid vector scaling using a convex combination

    alpha * dense + (1 - alpha) * sparse

    Args:
        dense: Array of floats representing
        sparse: a dict of `indices` and `values`
        alpha: float between 0 and 1 where 0 == sparse only
               and 1 == dense only
    """
    if alpha < 0 or alpha > 1:
        raise ValueError("Alpha must be between 0 and 1")
    # scale sparse and dense vectors to create hybrid search vecs
    hsparse = {
        'indices': sparse['indices'],
        'values':  [v * (1 - alpha) for v in sparse['values']]
    }
    hdense = [v * alpha for v in dense]
    return hdense, hsparse

def save_images(image_batch, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    saved_paths = []
    for i, img in enumerate(image_batch):
        image_path = os.path.join(output_folder, f"image_{i}.png")
        with open(image_path, "wb") as f:
            img.save(f, format='png')
        saved_paths.append(image_path)
    return saved_paths

# uncomment to upload vectors in db store

# status = upsert_documents()
# print(status)

# uncomment to create embeddings

# print("beginning to create sparse embeddings")
# create_sparse_embeddings()
# print("sparse embeddings created")

image_from_query = make_query("white shoes")


# Uncomment to save images in local directory 

image_batch = image_from_query# Your image batch
output_folder = r"C:\Users\ACER\Desktop\hackathons\Flipkart_Grid_SDET\output_images"
saved_image_paths = save_images(image_batch, output_folder)

for image_path in saved_image_paths:
    print("Image saved:", image_path)


