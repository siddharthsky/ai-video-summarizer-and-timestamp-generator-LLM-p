import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai



class Model():
    def __init__():
        pass

    def google_gemini(transcript,prompt):
        genai.configuration(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt+transcript)
        return response.text
