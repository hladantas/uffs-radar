import json
from playwright.sync_api import sync_playwright

# ---------------------------
# FUNÇÃO GENÉRICA PARA COLETAR PÁGINAS UFFS
# ---------------------------
def coletar_itens(url, seletor_item, seletor_titulo, seletor_link, seletor_data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Espera o conteúdo aparecer
        page.wait_for_selector(seletor_item)

        itens = page.query_selector_all(seletor_item)
        lista = []

        for item in itens:
            titulo = item.query_selector(seletor_titulo).inner_text() if item.query_selector(seletor_titulo) else ""
            link = item.query_selector(seletor_link).get_attribute("href") if item.query_selector(seletor_link) else ""
            data = item.query_selector(seletor_data).inner_text() if item.query_selector(seletor_data) else ""

            lista.append({
                "titulo": titulo,
                "link": link,
                "data": data
            })

        browser.close()
        return lista


# ---------------------------
# 1. NOTÍCIAS UFFS
# ---------------------------
def coletar_noticias():
    return coletar_itens(
        url="https://www.uffs.edu.br/uffs/acesso-rapido/noticias",
        seletor_item=".tileItem",
        seletor_titulo=".tileHeadline",
        seletor_link="a",
        seletor_data=".tileDate"
    )


# ---------------------------
# 2. BOLSAS E PROJETOS
# ---------------------------
def coletar_bolsas_projetos():
    return coletar_itens(
        url="https://www.uffs.edu.br/uffs/pesquisa/editais-1",
        seletor_item=".tileItem",
        seletor_titulo=".tileHeadline",
        seletor_link="a",
        seletor_data=".tileDate"
    )


# ---------------------------
# 3. EDITAIS ERECHIM (BOLETIM)
# ---------------------------
def coletar_editais_erechim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://boletim.uffs.edu.br/atos-normativos/edital/cer", timeout=60000)

        page.wait_for_selector("div.list-group a")

        itens = page.query_selector_all("div.list-group a")
        lista = []

        for item in itens:
            titulo = item.inner_text()
            link = item.get_attribute("href")
            if link.startswith("/"):
                link = "https://boletim.uffs.edu.br" + link

            lista.append({
                "titulo": titulo,
                "link": link,
                "data": ""
            })

        browser.close()
        return lista


# ---------------------------
# 4. BOLETIM GERAL
# ---------------------------
def coletar_boletim():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://boletim.uffs.edu.br/atos-normativos", timeout=60000)

        page.wait_for_selector("div.list-group a")

        itens = page.query_selector_all("div.list-group a")
        lista = []

        for item in itens:
            titulo = item.inner_text()
            link = item.get_attribute("href")
            if link.startswith("/"):
                link = "https://boletim.uffs.edu.br" + link

            lista.append({
                "titulo": titulo,
                "link": link,
                "data": ""
            })

        browser.close()
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
