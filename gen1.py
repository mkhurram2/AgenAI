
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
if not api_key:
    raise ValueError("API key is missing. Please check your .env file.")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("hi")
print(response.text)