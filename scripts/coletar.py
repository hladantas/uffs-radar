import requests
from bs4 import BeautifulSoup
import json
import os

BASE = "https://SEU-PROXY.onrender.com"  # coloque o endereço correto aqui

def pegar_html(endpoint):
    dados = requests.get(f"{BASE}/{endpoint}").json()
    return dados["html"]

def coletar_noticias():
    html = pegar_html("noticias")
    soup = BeautifulSoup(html, "html.parser")
    itens = soup.select(".tileItem")
    lista = []
    for item in itens:
        titulo = item.select_one(".tileHeadline").get_text(strip=True)
        link = item.select_one("a")["href"]
        data = item.select_one(".tileDate").get_text(strip=True)
        lista.append({"titulo": titulo, "link": link, "data": data})
    return lista

def coletar_editais():
    html = pegar_html("editais")
    soup = BeautifulSoup(html, "html.parser")
    itens = soup.select("div.list-group a")
    lista = []
    for item in itens:
        titulo = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://boletim.uffs.edu.br" + link
        lista.append({"titulo": titulo, "link": link})
    return lista

def coletar_boletim():
    html = pegar_html("boletim")
    soup = BeautifulSoup(html, "html.parser")
    itens = soup.select("div.list-group a")
    lista = []
    for item in itens:
        titulo = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://boletim.uffs.edu.br" + link
        lista.append({"titulo": titulo, "link": link})
    return lista

def coletar_bolsas():
    html = pegar_html("bolsas")
    soup = BeautifulSoup(html, "html.parser")
    itens = soup.select(".tileItem")
    lista = []
    for item in itens:
        titulo = item.select_one(".tileHeadline").get_text(strip=True)
        link = item.select_one("a")["href"]
        lista.append({"titulo": titulo, "link": link})
    return lista

def salvar():
    dados = {
        "noticias": coletar_noticias(),
        "editais": coletar_editais(),
        "boletim": coletar_boletim(),
        "bolsas": coletar_bolsas()
    }

    os.makedirs("dados", exist_ok=True)

    with open("dados/dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    salvar()
