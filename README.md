# Flipkart_Grid_SDET


Contents
---

* [Installation](#installation)
* [Tech-Stacks Used](#tech-stacks-used)
* [Features Added](#use-cases)
* [Future Scope](#future-scope)
* [Snapshots](#snapshots)
* [Deployed Link](#deployed-link)

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
- Azure
