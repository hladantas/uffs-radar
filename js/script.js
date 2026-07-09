fetch("dados.json")
  .then(response => response.json())
  .then(dados => {
    
    // Notícias
    const noticiasUl = document.getElementById("noticias");
    dados.noticias.forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = `<a href="${item.link}" target="_blank">${item.titulo}</a>`;
      noticiasUl.appendChild(li);
    });

    // Editais
    const editaisUl = document.getElementById("editais");
    dados.editais.forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = `<a href="${item.link}" target="_blank">${item.titulo}</a>`;
      editaisUl.appendChild(li);
    });

    // Boletins
    const boletimUl = document.getElementById("boletim");
    dados.boletim.forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = `<a href="${item.link}" target="_blank">${item.titulo}</a>`;
      boletimUl.appendChild(li);
    });

    // Bolsas
    const bolsasUl = document.getElementById("bolsas");
    dados.bolsas.forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = `<a href="${item.link}" target="_blank">${item.titulo}</a>`;
      bolsasUl.appendChild(li);
    });

  })
  .catch(err => console.error("Erro ao carregar dados:", err));
