from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("API key is missing. Please check your .env file.")

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key
)
result = llm.invoke("Hi, What is the capital of pakistan?") 

print(result)
