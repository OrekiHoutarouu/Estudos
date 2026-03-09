const path = require("path")
const escrever = require("./modules/escrever")
const ler = require("./modules/ler")

const caminho_arquivo = path.resolve(__dirname, "teste.json")

const pessoas = [
    {nome: "João", idade: 23},
    {nome: "Maria", idade: 18},
    {nome: "Marcos", idade: 16},
    {nome: "Emília", idade: 55}
]

const json = JSON.stringify(pessoas, "", 2)

escrever(caminho_arquivo, json)

async function le_arquivo(caminho) {
    const dados = await ler(caminho)
    return dados
}

le_arquivo(caminho_arquivo)
    .then(dados => {
        dados = JSON.parse(dados)

        for (dado of dados) {
            console.log(dado)
        }
    })