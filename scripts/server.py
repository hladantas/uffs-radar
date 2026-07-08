from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

def fetch_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")
        html = page.content()
        browser.close()
        return html

@app.route("/noticias")
def noticias():
    html = fetch_html("https://www.uffs.edu.br/uffs/acesso-rapido/noticias")
    return jsonify({"html": html})

@app.route("/editais")
def editais():
    html = fetch_html("https://boletim.uffs.edu.br/atos-normativos/edital/cer")
    return jsonify({"html": html})

@app.route("/boletim")
def boletim():
    html = fetch_html("https://boletim.uffs.edu.br/atos-normativos")
    return jsonify({"html": html})

@app.route("/bolsas")
def bolsas():
    html = fetch_html("https://www.uffs.edu.br/uffs/pesquisa/editais-1")
    return jsonify({"html": html})

@app.route("/")
def home():
    return "Servidor proxy UFFS funcionando!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
