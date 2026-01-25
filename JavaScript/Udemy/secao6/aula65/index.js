function Pessoa(nome, sobrenome) {
    this.nome = nome
    this.sobrenome = sobrenome
}

Pessoa.prototype.nome_completo = function () {
    return `${this.nome} ${this.sobrenome}`
}

const pessoa1 = new Pessoa("Samuel", "Campelo")
const pessoa2 = new Pessoa("Matheus", "Levi")

console.log(pessoa1.nome_completo())
console.log(pessoa2.nome_completo())