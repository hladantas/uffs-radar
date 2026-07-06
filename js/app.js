async function carregarDados(tipo) {
    const area = document.getElementById("conteudo");

    try {
        const resposta = await fetch("dados/dados.json");
        const dados = await resposta.json();

        const lista = dados[tipo];

        let html = "<ul>";

        lista.forEach(item => {
            html += `
                <li>
                    <strong>${item.titulo}</strong><br>
                    <a href="${item.link}" target="_blank">Acessar</a><br>
                    <small>${item.data}</small>
                </li>
                <hr>
            `;
        });

        html += "</ul>";

        area.innerHTML = html;

    } catch (erro) {
        area.innerHTML = "<p>Erro ao carregar dados.</p>";
    }
}
