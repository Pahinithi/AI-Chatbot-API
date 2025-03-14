import os
import json
import google.generativeai as genai

# Load configuration
config_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "config.json"
)
with open(config_file_path) as config_file:
    config_data = json.load(config_file)

# Configure API key
genai.configure(api_key=config_data["GOOGLE_API_KEY"])


def gemini_pro_vision_response(prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    return response.text


def embeddings_model_response(input_text):
    embedding = genai.embed_content(
        model="models/embedding-001", content=input_text, task_type="retrieval_document"
    )
    return embedding["embedding"]


def gemini_pro_response(user_prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_prompt)
    return response.text


def gemini_pro_sport_response(sport_query):  # New function
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(sport_query)
    return response.text
