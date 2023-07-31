import os
from dotenv import load_dotenv
import openai

#load the api key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#interact with gpt
def gpt_chat(text):
    print(text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        max_tokens=200, 
    )
    return response['choices'][0]['message']['content']


