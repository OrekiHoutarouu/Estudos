const elementos = [
    {tag: "p", texto: "Isso é um parágrafo"},
    {tag: "div", texto: "Isso é uma div"},
    {tag: "section", texto: "Isso é uma section"},
    {tag: "footer", texto: "Isso é um footer"},
]

const container = document.querySelector(".container")
const div = document.createElement("div")

for (let c = 0; c < elementos.length; c++) {
    let {tag, texto} = elementos[c]
    let tag_criada = document.createElement(tag)

    tag_criada.innerText = texto
    div.appendChild(tag_criada)
}

container.appendChild(div)