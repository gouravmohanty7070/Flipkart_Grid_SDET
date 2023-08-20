from django.shortcuts import render
from django.http import JsonResponse
from utils.LLM import get_query_from_text
from django.views.decorators.csrf import csrf_exempt
from utils.queries import make_query, get_query_from_text, load_model, load_sparse_embeddings, create_images_and_metadata
import json
import re
import base64
from io import BytesIO


@csrf_exempt
def get_recommendation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get('text', '')
        print('yes baby i am here')
        print(data)
        print(type(data))
        print(user_input)
        print(len(user_input))
        response_data = get_query_from_text(user_input)
        # response_data = response_data[9:-10]

        print(response_data)  # your function
        image_recommendations = get_image_recommendations_for_outfit(
            response_data)
        return JsonResponse(image_recommendations)
    else:
        return JsonResponse({"error": "POST request expected."})


def image_to_base64(img):
    """
    Converts an image or the first image from a list of images to base64.
    """
    buffered = BytesIO()

    # If img is a list, work with the first image
    if isinstance(img, list):
        img = img[0]

    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def extract_outfit_details(input_text):
    print("extracting")
    print(input_text)
    # Step 1: Extract content between <OUTFIT> tags
    outfit_content_pattern = r"<OUTFIT>\s*(.*?)\s*<\/OUTFIT>"
    match = re.search(outfit_content_pattern, input_text, re.DOTALL)
    print(match)

    if match is None:
        return {}

    outfit_content = match.group(1)

    # Step 2: Extract individual details from outfit_content
    def extract_detail(pattern, text):
        match = re.search(pattern, text)
        return match.group(1) if match else ""

    topwear = extract_detail(r'"topwear":\s*"(.*?)"', outfit_content)
    bottomwear = extract_detail(r'"bottomwear":\s*"(.*?)"', outfit_content)
    footwear = extract_detail(r'"footwear":\s*"(.*?)"', outfit_content)
    accessories = extract_detail(r'"accessories":\s*"(.*?)"', outfit_content)

    details = {
        "topwear": topwear,
        "bottomwear": bottomwear,
        "footwear": footwear,
        "accessories": accessories
    }

    print(details)
    return details


def get_image_recommendations_for_outfit(input_text):
    outfit_details = extract_outfit_details(input_text)
    print("Outfit Details:", outfit_details)
    images = {}
    print("imageDone")

    for category, description in outfit_details.items():
        query_sparse = description
        query_dense = get_query_from_text(description)

        # Using the make_query function to get image results.
        image_results = make_query(query_sparse, query_dense)

        if image_results:
            images[category] = image_to_base64(image_results)
    return images


def chat_view(request):
    return render(request, 'chat/chat.html')
