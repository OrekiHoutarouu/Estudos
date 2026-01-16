function Produto(nome, preco, estoque) {
    Object.defineProperty(this, "estoque", {
        enumerable: true,
        value: estoque,
        writable: false,
        configurable: false
    })

    Object.defineProperties(this, {
        nome: {
            enumerable: true,
            value: nome,
            writable: true,
            configurable: true
        },

        preco: {
            enumerable: true,
            value: preco,
            writable: true,
            configurable: true
        }
    }) 
}

const produto1 = new Produto("Camiseta", 20, 3)
console.log(produto1)