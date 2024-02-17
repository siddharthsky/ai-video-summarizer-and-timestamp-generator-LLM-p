import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI 

class Model:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def google_gemini(transcript, prompt, extra=""):
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + extra + transcript)
        return response.text
    
    @staticmethod
    def openai_chatgpt(transcript, prompt, extra=""):
        client =   OpenAI(api_key=os.getenv("OPENAI_CHATPGPT_API_KEY2"))
        model="gpt-3.5-turbo"
        message = [{"role": "system", "content": prompt + extra + transcript}]
        response = client.chat.completions.create(model=model, messages=message)
        return response.choices[0].message.content
