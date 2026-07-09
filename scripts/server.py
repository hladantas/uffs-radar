from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL_NOTICIAS = "https://www.uffs.edu.br/uffs/acesso-rapido/noticias?categoria=Erechim"
URL_EDITAIS = "https://boletim.uffs.edu.br/atos-normativos/edital/cer"
URL_BOLETIM = "https://boletim.uffs.edu.br/atos-normativos"
URL_BOLSAS = "https://www.uffs.edu.br/uffs/pesquisa/editais-1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

def pegar_html(url):
    resposta = requests.get(url, headers=HEADERS, timeout=10)
    resposta.raise_for_status()
    return resposta.text

@app.route("/")
def raiz():
    return jsonify({"status": "ok", "mensagem": "Proxy UFFS ativo"})

@app.route("/noticias")
def noticias():
    try:
        return jsonify({"html": pegar_html(URL_NOTICIAS)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/editais")
def editais():
    try:
        return jsonify({"html": pegar_html(URL_EDITAIS)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/boletim")
def boletim():
    try:
        return jsonify({"html": pegar_html(URL_BOLETIM)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/bolsas")
def bolsas():
    try:
        return jsonify({"html": pegar_html(URL_BOLSAS)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
