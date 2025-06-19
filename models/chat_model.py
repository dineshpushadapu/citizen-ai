import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from utils.text_cleaning import clean_text  # Import the cleaning utility

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API token from environment
api_key = os.getenv("HF_API_TOKEN")

# Ensure the token is available
if not api_key:
    raise ValueError("Hugging Face API token not found in environment variables.")

# Initialize the inference client
client = InferenceClient(
    model="deepseek-ai/DeepSeek-R1-0528",
    token=api_key
)

def generate_response(user_input):
    cleaned_input = clean_text(user_input)  # Clean the input
    completion = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": cleaned_input
            }
        ],
    )
    return completion.choices[0].message["content"]

# For testing directly in terminal
