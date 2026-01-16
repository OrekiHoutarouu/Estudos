function Produto(nome, preco, estoque) {
    let estoque_privado = estoque

    Object.defineProperty(this, "estoque", {
        enumerable: true,
        configurable: false,

        get: function() {
            return estoque_privado
        },

        set: function(valor) {
            if(typeof valor !== "number") {
                throw new TypeError("Estoque tem que ser um número")
            }

            estoque_privado = valor
        },
    })

    this.nome = nome
    this.preco = preco
}

const produto1 = new Produto("Camiseta", 20, 3)
produto1.estoque = "blablabla"
console.log(produto1)
console.log(produto1.estoque)