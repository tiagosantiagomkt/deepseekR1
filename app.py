import torch
from fastapi import FastAPI
from transformers import AutoTokenizer
from vllm import LLM
from pydantic import BaseModel

# Inicializando o FastAPI
app = FastAPI()

# Carregar o modelo e o tokenizador
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = LLM.from_pretrained(model_name)

# Definir um modelo de entrada para a requisição
class PromptRequest(BaseModel):
    prompt: str

# Função para gerar resposta
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(inputs["input_ids"], max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Rota para gerar resposta via API
@app.post("/generate")
def generate(prompt_request: PromptRequest):
    prompt = prompt_request.prompt
    response = generate_response(prompt)
    return {"response": response}

# Rota de saúde (para verificar se o serviço está funcionando)
@app.get("/health")
def health_check():
    return {"status": "healthy"}
