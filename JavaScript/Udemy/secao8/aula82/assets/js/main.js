// fetch("pessoas.json")
//     .then(resposta => resposta.json())
//     .then(json => carrega_elementos(json))

axios("pessoas.json")
    .then(resposta => carrega_elementos(resposta.data))

function carrega_elementos(json) {
    const resultado = document.querySelector("#resultado")
    const table = document.createElement("table")

    for (let pessoa of json) {
        const tr = document.createElement("tr")

        let td = document.createElement("td")
        td.innerHTML = pessoa.nome
        tr.appendChild(td)

        td = document.createElement("td")
        td.innerHTML = `R$ ${pessoa.salario}`
        tr.appendChild(td)

        td = document.createElement("td")
        td.innerHTML = `${pessoa.idade} anos`
        tr.appendChild(td)

        table.appendChild(tr)
    }

    resultado.appendChild(table)
}