# Imagem base
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta e comando de execução
EXPOSE 5000
CMD ["python", "app.py"]
