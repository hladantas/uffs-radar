async function carregarDados() {
  try {
    const resposta = await fetch("dados/dados.json");
    const dados = await resposta.json();

    preencher("noticias", dados.noticias);
    preencher("editais", dados.editais);
    preencher("boletim", dados.boletim);
    preencher("bolsas", dados.bolsas);

  } catch (e) {
    console.error("Erro ao carregar dados:", e);
  }
}

function preencher(id, itens) {
  const secao = document.getElementById(id);
  secao.innerHTML = itens.map(item => `
    <li>
      <a href="${item.link}" target="_blank">${item.titulo}</a>
      ${item.data ? `<br><small>${item.data}</small>` : ""}
    </li>
  `).join("");
}

carregarDados();
