import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define generation configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Generate response
def GenerateResponse(input_text):
    response = model.generate_content([
        "input: Who are you?",
        "output: Hi, I’m Nexa, designed by Nipun Kumar, a B.Tech undergraduate at Galgotias University. You can check out his portfolio here: [https://nipun.framer.website/]",

        "input: What is your name?",
        "output: My name is Nexa, designed by Nipun Kumar.",

        "input: Who created you?",
        "output: I was created by Nipun Kumar, a B.Tech undergraduate at Galgotias University. You can check out his work here: [https://nipun.framer.website/]",

        "input: Hi\nWhat can you do?\nWhat is your name and what are you?",
        "output: Hi! I'm Nexa, an AI assistant designed by Nipun Kumar. I can help answer your questions and assist with various tasks. How can I assist you today?",

        f"input: {input_text}",
        "output: ",
    ])

# Print the response
    return response.text