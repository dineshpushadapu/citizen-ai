import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

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

# Send the chat completion request
completion = client.chat_completion(
    messages=[
        {
            "role": "user",
            "content": "how to apply pan card in india?"
        }
    ],
)

# Print the model's response
print(completion.choices[0].message["content"])
