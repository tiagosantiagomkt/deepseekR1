import torch
from transformers import AutoTokenizer
from vllm import LLM

# Carregar o modelo e o tokenizador
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = LLM.from_pretrained(model_name)

# Função para gerar resposta
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(inputs["input_ids"], max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Exemplo de uso
prompt = "Qual é a capital da França?"
response = generate_response(prompt)
print(response)
