from flask import Flask, request
import logging
from datetime import datetime
import os

# Criar pasta de logs caso não exista
os.makedirs("logs", exist_ok=True)

# Configuração de logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Rota / acessada com sucesso")
    return {"message": "Aplicação Python funcionando com sucesso!"}

@app.route("/teste")
def teste():
    logging.info("Rota /teste acessada")
    return {"message": "Teste de logging"}

@app.route("/erro")
def erro():
    logging.error("Rota /erro acessada - simulação de erro")
    return {"message": "Erro simulado"}, 500

if __name__ == "__main__":
    logging.info("Aplicação iniciada")
    app.run(host="0.0.0.0", port=5000)
