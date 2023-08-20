import re
import json


def extract_outfit_details(input_text):
    # print("extractDone")
    outfit_pattern = r"<OUTFIT>([\s\S]*?)<\/OUTFIT>"
    # print(outfit_pattern)
    match = re.search(outfit_pattern, input_text)
    # print(match)
#     if not match:
#         return {}

    details = match.group(1).strip()
    # details = dict(details)
    details = '{'+details+'}'
    details = json.loads(details)
    print(details)
    print(type(details))
    return details


it = """A winter suit for a beach party can be a unique and stylish choice. Since it's a beach party, you'll want to incorporate elements that are both warm and beach-appropriate. I recommend a cozy and trendy outfit that will keep you comfortable  still looking fashionable.

For the topwear, a chunky knit sweater in a neutral color, such as cream or light gray, would be perfect. It will provide warmth while giving off a relaxed and beachy vibe. Pair it with a stylish pair of slim-fit navy blue trousers for a polished look.

To complete the outfit, opt for a pair of suede desert boots in a light tan color. They will not only keep your feet warm but also add a touch of sophistication to the overall ensemble.

Since it's a beach party, accessorize with a woven straw fedora hat to protect yourself from the sun and add a trendy flair to the outfit.

Here's the personalized outfit recommendation for your winter beach party:

<OUTFIT>
"topwear": "Chunky knit sweater in cream",
"bottomwear": "Navy blue slim-fit trousers",
"footwear": "Light tan suede desert boots",
"accessories": "Woven straw fedora hat"
</OUTFIT>

Feel free to let me know if there's anything specific you'd like to change or if you need further assistance!
imageDone
"""
extract_outfit_details(it)
