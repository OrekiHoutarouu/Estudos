const objeto = {
    letra: "A"
}

const objeto2 = {
    letra2: "B"
}

const objeto3 = {
    letra3: "C"
}

Object.setPrototypeOf(objeto2, objeto)
Object.setPrototypeOf(objeto3, objeto2)
console.log(objeto2.letra, objeto2.letra2)
console.log(objeto3.letra, objeto3.letra2, objeto3.letra3)


function Produto(nome, preco) {
    this.nome = nome
    this.preco = preco
}

Produto.prototype.desconto = function(percentual) {
    this.preco = this.preco - (this.preco * (percentual / 100))
} 

Produto.prototype.aumento = function(percentual) {
    this.preco = this.preco + (this.preco * (percentual / 100))
} 

const produto = new Produto("Caneca", 7.99)

produto.desconto(50)

console.log(produto)