import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configuration(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))


class Model():
    def __init__():
        pass

    def google_gemini(transcript,prompt):
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt+transcript)
        return response.text
