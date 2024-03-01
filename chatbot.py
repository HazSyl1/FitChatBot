from peft import AutoPeftModelForCausalLM
from transformers import GenerationConfig
from transformers import AutoTokenizer
import torch
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".env" , override=True)
token = os.getenv("HF_TOKEN")
tokenizer=AutoTokenizer.from_pretrained("HazSylvia/Fitness_Trained_Gemma_2b",token=token)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


model=AutoPeftModelForCausalLM.from_pretrained(
    "HazSylvia/Fitness_Trained_Gemma_2b",
    low_cpu_mem_usage=True,
    return_dict=True,
    torch_dtype=torch.float16,
    device_map=device,
    token=token
    )
generation_config=GenerationConfig(
    do_sample=True,
    top_k=1,
    temperature=0.2,
    max_new_tokens=100,
    pad_token_id=tokenizer.eos_token_id
)
    
def chatbot(message):  
  print("Generating Response!")
  input_str="Human:"+message+"\nAssistant:"
  inputs=tokenizer(input_str,return_tensors="pt").to(device)
  outputs=model.generate(**inputs ,generation_config=generation_config)
  return tokenizer.decode(outputs[0],skip_special_tokens=True).replace(input_str,"")
