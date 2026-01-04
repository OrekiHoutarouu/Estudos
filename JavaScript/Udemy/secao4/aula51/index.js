function Pessoa(nome, sobrenome) {
    this.nome = nome
    this.sobrenome = sobrenome

    this.metodo = function() {
        console.log("Sou um método")
    }
}

const pessoa1 = new Pessoa("Samuel", "Campelo")
const pessoa2 = new Pessoa("Campelo", "Samuel")

console.log(pessoa1.nome)