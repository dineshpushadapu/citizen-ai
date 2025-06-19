import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from utils.text_cleaning import clean_text  # Correct utility import

# Load environment variables
load_dotenv()

# Get Hugging Face API token
api_key = os.getenv("api_token")
if not api_key:
    raise ValueError("Hugging Face API token not found. Please set it in your .env file.")

# Initialize client
client = InferenceClient(token=api_key)

# Label mapping
label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}

# Analyze sentiment
def analyze_sentiment(text):
    cleaned_text = clean_text(text)
    result = client.text_classification(cleaned_text, model="cardiffnlp/twitter-roberta-base-sentiment")
    label = label_map.get(result[0]["label"], result[0]["label"])
    return label
