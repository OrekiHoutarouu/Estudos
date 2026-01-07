const numeros = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27]

const maior_que_dez = numeros.filter(valor => valor > 10)

console.log(maior_que_dez)

const pessoas = [
    {nome: "Samuel", idade: 16},
    {nome: "Maria", idade: 23},
    {nome: "Eduardo", idade: 55},
    {nome: "Letícia", idade: 19},
    {nome: "Rosana", idade: 32},
    {nome: "Wallace", idade: 47}
]

const pessoas_cinco_letras_nome = pessoas.filter(pessoa => pessoa.nome.length > 5)
console.log(pessoas_cinco_letras_nome)

const pessoas_mais_cinquenta_anos = pessoas.filter(pessoa => pessoa.idade > 50)
console.log(pessoas_mais_cinquenta_anos)

const pessoas_nome_terminado_a = pessoas.filter(pessoa => pessoa.nome.toLowerCase().endsWith("a"))
console.log(pessoas_nome_terminado_a)