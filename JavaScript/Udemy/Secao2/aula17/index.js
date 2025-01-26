const pessoa1 = {
    nome: "Samuel",
    sobrenome: "Campelo",
    idade: 15,

    fala() {
        return `Olá, eu me chamo ${this.nome} e eu tenho ${this.idade} anos.`
    },

    incrementaIdade() {
        return ++this.idade
    }
}

console.log(pessoa1.fala())
console.log(pessoa1.incrementaIdade())

function cria_pessoa(nome, sobrenome, idade) {
    return {nome, sobrenome, idade}
}

const pessoa2 = cria_pessoa("Luiz", "Otávio", 25)
console.log(pessoa2)

const pessoa3 = cria_pessoa("João", "Guilherme", 32)
console.log(pessoa3)

const pessoa4 = cria_pessoa("Maria", "Antônia", 13)
console.log(pessoa4)

const pessoa5 = cria_pessoa("Luana", "Gonçalves", 22)
console.log(pessoa5)