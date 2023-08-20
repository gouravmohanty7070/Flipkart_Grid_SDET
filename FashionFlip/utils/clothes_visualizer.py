import replicate
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

def clothes_visualizer(prompt):
    output = replicate.run(
        "naklecha/fashion-ai:4e7916cc6ca0fe2e0e414c32033a378ff5d8879f209b1df30e824d6779403826",
        input={"image": open(r"C:\Users\ACER\Desktop\hackathons\Flipkart_Grid_SDET\image.jpg", "rb"), "clothing": "topwear", "prompt": prompt}
    )
    return output