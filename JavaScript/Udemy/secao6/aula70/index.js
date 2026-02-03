function cria_pessoa(nome, sobrenome) {
    const pessoa_prototype = {
        falar() {
            console.log(`${this.nome} está falando`)
        },
        
        comer() {
            console.log(`${this.nome} está comendo`)
        },
    
        beber() {
            console.log(`${this.nome} está bebendo`)
        },
    }
    
    return Object.create(pessoa_prototype, {
        nome: {value: nome},
        sobrenome: {value: sobrenome}
    })
}

const pessoa1 = cria_pessoa("Samuel", "Campelo")
console.log(pessoa1)
pessoa1.comer()