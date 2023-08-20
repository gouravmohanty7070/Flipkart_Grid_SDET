![Capture](https://res.cloudinary.com/dhhax6yae/image/upload/v1692450139/Screenshot_2023-08-19_at_6.27.34_PM_miqrv9.png)

# FashionFlip
---

`FashionFlip` is the breakthrough you've been waiting for to transform your fashion experience. In a world where style matters, we're introducing a fresh approach that blends technology with individuality.

Say hello to AI-powered visual searches, lifelike outfit previews, and a personalized stylist, Mona. Step into a new realm of fashion discovery with FashionFlip. Your style, your way.



Contents
---

* [Installation](#installation)
* [Tech-Stacks Used](#tech-stacks-used)
* [Features Added](#use-cases)
* [Demo](#demo)

### Installation:
---
#### Setup Virtual Environment

To ensure a clean and isolated environment for your application, it's recommended to use a virtual environment. Here's how you can set it up:

```
cd {your-repo}
python -m virtualenv venv
```
Activating the Virtual Environment
- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:

```
source venv/bin/activate
```

#### Install Dependencies
With the virtual environment activated, install the required dependencies using pip and the requirements.txt file:
```
pip install -r requirements.txt
```
#### Setup .env
To run the LLM we need to create a .env file and add our openai api key to it 

```
OPENAI_API_KEY = "{your_api_key}"
```

#### Start the Application
Navigate to the "FashionFlip" directory, which contains the application code:
```
cd FashionFlip
```

Run the following command to start the application:
```
python manage.py runserver
```

#### Access the Application
Open your web browser and go to http://127.0.0.1:8000/ 

### Tech-Stacks Used:
---

- Python
- LangChain
- OpenAI
- Django
- Javascript
- Pinecone

### Use Cases
---
<ol>
<li>Explore New Styles, Your Way:
Embrace style evolution effortlessly. Personalized outfit ideas blend trends and your unique taste, inspiring fashion exploration.</li></br>
<li>Instant Party-Ready Confidence:
Arrive prepared at last-minute events. FashionFlip's visual search matches themes, ensuring your confidence shines through in style.
</li></br>
<li>Stay Stylish in Any Weather:
Effortlessly navigate seasons. Specify preferences and colors, allowing FashionFlip to curate chic outfits tailored to weather conditions.
</li></br>
<li>Effortless Packing for Adventures:
Simplify travel preparation. Share trip details for curated, versatile outfits. Travel light while staying fashion-forward with FashionFlip.
</li></br>
</ol>

--------
### Demo
---

[Demo Video](https://drive.google.com/file/d/1q9u5K001zdps-9WpUBGXJZHVkTzW2s9u/view?usp=sharing)

