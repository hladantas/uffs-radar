from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL_NOTICIAS = "https://www.uffs.edu.br/campi/erechim/noticias"
URL_EDITAIS = "https://boletim.uffs.edu.br/publico/erechim/editais"
URL_BOLETIM = "https://boletim.uffs.edu.br/publico/erechim/boletins"
URL_BOLSAS = "https://www.uffs.edu.br/campi/erechim/projetos"

def pegar_html(url):
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.text

@app.route("/")
def raiz():
    return jsonify({"status": "ok", "mensagem": "Proxy UFFS ativo"})

@app.route("/noticias")
def noticias():
    return jsonify({"html": pegar_html(URL_NOTICIAS)})

@app.route("/editais")
def editais():
    return jsonify({"html": pegar_html(URL_EDITAIS)})

@app.route("/boletim")
def boletim():
    return jsonify({"html": pegar_html(URL_BOLETIM)})

@app.route("/bolsas")
def bolsas():
    return jsonify({"html": pegar_html(URL_BOLSAS)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
