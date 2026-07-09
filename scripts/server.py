from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URLs reais da UFFS
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
    html = pegar_html(URL_NOTICIAS)
    return jsonify({"html": html})

@app.route("/editais")
def editais():
    html = pegar_html(URL_EDITAIS)
    return jsonify({"html": html})

@app.route("/boletim")
def boletim():
    html = pegar_html(URL_BOLETIM)
    return jsonify({"html": html})

@app.route("/bolsas")
def bolsas():
    html = pegar_html(URL_BOLSAS)
    return jsonify({"html": html})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
