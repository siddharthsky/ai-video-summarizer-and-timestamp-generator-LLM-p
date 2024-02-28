import os
from dotenv import load_dotenv
import google.generativeai as genai

class Model:
    def __init__(self):
        load_dotenv() # Load environment variables from .env file

    @staticmethod
    def google_gemini(transcript, prompt, extra=""):
        load_dotenv() 
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + extra + transcript)
        return response.text
