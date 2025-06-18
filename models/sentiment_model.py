import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env
load_dotenv()

# Get Hugging Face API token
api_key = os.getenv("api_token")
if not api_key:
    raise ValueError("Hugging Face API token not found. Please set HF_TOKEN in your .env file.")

# Initialize the client
client = InferenceClient(token=api_key)

# Sentiment analysis
text = "I like you. I love you."
model_name = "cardiffnlp/twitter-roberta-base-sentiment"

# Get result
result = client.text_classification(text, model=model_name)

# Convert label to readable format
label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}
label = label_map.get(result[0]["label"], result[0]["label"])

# Output the result
print(label)
