import requests
from bs4 import BeautifulSoup
import json

# URLs do proxy
URL_NOTICIAS = "https://uffs-radar.onrender.com/noticias"
URL_EDITAIS = "https://uffs-radar.onrender.com/editais"
URL_BOLETIM = "https://uffs-radar.onrender.com/boletim"
URL_BOLSAS = "https://uffs-radar.onrender.com/bolsas"

def pegar_html(url):
    """Busca HTML do proxy e retorna o conteúdo."""
    resposta = requests.get(url, timeout=15)
    resposta.raise_for_status()
    dados = resposta.json()
    return dados["html"]

def extrair_links_noticias(html):
    """Extrai links das notícias do Portal UFFS."""
    soup = BeautifulSoup(html, "html.parser")
    itens = []

    for card in soup.select("div.card-noticia"):
        titulo = card.select_one("h3")
        link = card.select_one("a")

        if titulo and link:
            itens.append({
                "titulo": titulo.get_text(strip=True),
                "link": link["href"]
            })

    return itens

def extrair_links_editais(html):
    """Extrai links dos editais do boletim."""
    soup = BeautifulSoup(html, "html.parser")
    itens = []

    for linha in soup.select("table tbody tr"):
        link_tag = linha.select_one("a")
        if link_tag:
            itens.append({
                "titulo": link_tag.get_text(strip=True),
                "link": link_tag["href"]
            })

    return itens

def extrair_links_boletim(html):
    """Extrai links dos boletins."""
    soup = BeautifulSoup(html, "html.parser")
    itens = []

    for link_tag in soup.select("a"):
        href = link_tag.get("href", "")
        if "boletim" in href:
            itens.append({
                "titulo": link_tag.get_text(strip=True),
                "link": href
            })

    return itens

def extrair_links_bolsas(html):
    """Extrai links de bolsas e projetos."""
    soup = BeautifulSoup(html, "html.parser")
    itens = []

    for link_tag in soup.select("a"):
        href = link_tag.get("href", "")
        if "editais" in href or "projeto" in href:
            itens.append({
                "titulo": link_tag.get_text(strip=True),
                "link": href
            })

    return itens

def salvar_json(dados):
    """Salva o arquivo dados.json."""
    with open("dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def main():
    print("Coletando dados...")

    noticias_html = pegar_html(URL_NOTICIAS)
    editais_html = pegar_html(URL_EDITAIS)
    boletim_html = pegar_html(URL_BOLETIM)
    bolsas_html = pegar_html(URL_BOLSAS)

    dados = {
        "noticias": extrair_links_noticias(noticias_html),
        "editais": extrair_links_editais(editais_html),
        "boletim": extrair_links_boletim(boletim_html),
        "bolsas": extrair_links_bolsas(bolsas_html)
    }

    salvar_json(dados)
    print("Arquivo dados.json atualizado com sucesso!")

if __name__ == "__main__":
    main()
