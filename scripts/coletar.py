import requests
from bs4 import BeautifulSoup
import json
import os

# ENDEREÇO CORRETO DO PROXY
BASE = "https://uffs-radar.onrender.com"

def pegar_html(endpoint):
    resposta = requests.get(f"{BASE}/{endpoint}")
    resposta.raise_for_status()  # se der erro, o workflow mostra
    dados = resposta.json()
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
            link = "https://boletim.uffs.edu
