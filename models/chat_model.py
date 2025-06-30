
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
import torch
from utils.text_cleaning import clean_text

class ChatModel:
    def __init__(self, model_path="ibm-granite/granite-3.3-8b-instruct"):
        self.model_path = model_path
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map=self.device,
            torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    def generate_text(self, prompt, max_new_tokens=1024, seed=42):
        conv = [{"role": "user", "content": prompt}]
        input_ids = self.tokenizer.apply_chat_template(
            conv,
            return_tensors="pt",
            thinking=True,
            return_dict=True,
            add_generation_prompt=True
        ).to(self.device)
        set_seed(seed)
        output = self.model.generate(
            **input_ids,
            max_new_tokens=max_new_tokens,
        )
        prediction = self.tokenizer.decode(
            output[0, input_ids["input_ids"].shape[1]:],
            skip_special_tokens=True
        )
        return prediction

chat_model = ChatModel()


def generate_response(user_input):
    try:
        cleaned_input = clean_text(user_input)
        response = chat_model.generate_text(cleaned_input)
        return response
    except Exception as e:
        print("[ERROR in generate_response]:", e)
        return "Sorry, I couldn't process your request right now."
