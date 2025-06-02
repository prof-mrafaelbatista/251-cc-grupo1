# Setar o ambiente de desenvolvimento
FROM python:3.11-slim

WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000
EXPOSE 5000
CMD ["python3","-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]