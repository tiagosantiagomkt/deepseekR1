FROM python:3.10-slim

WORKDIR /app

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código fonte para o container
COPY . .

# Expondo a porta para o servidor
EXPOSE 3000

# Comando para iniciar o servidor
CMD ["python", "app.py"]
