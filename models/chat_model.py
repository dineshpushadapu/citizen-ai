from transformers import AutoModelForCausalLM, AutoTokenizer,pipeline,BitsAndBytesConfig
import torch
    
# models/chat_model.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, BitsAndBytesConfig

class ChatModel:
    def __init__(self, model_name="ibm/granite-13b-chat-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype="float16",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            quantization_config=quant_config
        )
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def get_response(self, prompt):
        output = self.pipeline(prompt, max_new_tokens=150, do_sample=True, temperature=0.7)
        return output[0]['generated_text']
    
    

      
