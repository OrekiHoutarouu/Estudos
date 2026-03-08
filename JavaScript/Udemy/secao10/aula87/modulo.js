const fala_nome = (nome, sobrenome) => `${nome} ${sobrenome}`

exports.fala_nome = fala_nome

class Pessoa {
    constructor(nome) {
        this.nome = nome
    }
}

exports.Pessoa = Pessoa