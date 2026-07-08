import requests
from bs4 import BeautifulSoup
import json

# ---------------------------
# 1. EDITAIS ERECHIM (BOLETIM)
# ---------------------------
def coletar_editais_erechim():
    url = "https://boletim.uffs.edu.br/atos-normativos/edital/cer"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    lista = []

    for item in soup.select("div.list-group a"):
        titulo = item.get_text(strip=True)
        link = item["href"]
        data = ""  # página não exibe data diretamente

        lista.append({
            "titulo": titulo,
            "link": link,
            "data": data
        })

    return lista


# ---------------------------
# 2. NOTÍCIAS UFFS
# ---------------------------
def coletar_noticias():
    url = "https://www.uffs.edu.br/uffs/acesso-rapido/noticias?categoria="
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    lista = []

    for item in soup.select(".tileItem"):
        titulo = item.select_one(".tileHeadline").get_text(strip=True)
        link = item.select_one("a")["href"]
        data = item.select_one(".tileDate").get_text(strip=True)

        lista.append({
            "titulo": titulo,
            "link": link,
            "data": data
        })

    return lista


# ---------------------------
# 3. BOLETIM GERAL (ATOS NORMATIVOS)
# ---------------------------
def coletar_boletim():
    url = "https://boletim.uffs.edu.br/atos-normativos"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    lista = []

    for item in soup.select("div.list-group a"):
        titulo = item.get_text(strip=True)
        link = item["href"]
        data = ""  # página não exibe data diretamente

        lista.append({
            "titulo": titulo,
            "link": link,
            "data": data
        })

    return lista


# ---------------------------
# 4. BOLSAS E PROJETOS
# ---------------------------
def coletar_bolsas_projetos():
    url = "https://www.uffs.edu.br/uffs/pesquisa/editais-1"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    lista = []

    for item in soup.select(".tileItem"):
        titulo = item.select_one(".tileHeadline").get_text(strip=True)
        link = item.select_one("a")["href"]
        data = item.select_one(".tileDate").get_text(strip=True)

        lista.append({
            "titulo": titulo,
            "link": link,
            "data": data
        })

    return lista


# ---------------------------
# SALVAR JSON FINAL
# ---------------------------
def salvar_json():
    dados = {
        "editais": coletar_editais_erechim(),
        "noticias": coletar_noticias(),
        "boletim": coletar_boletim(),
        "bolsas_projetos": coletar_bolsas_projetos()
    }

    with open("dados/dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    salvar_json()
