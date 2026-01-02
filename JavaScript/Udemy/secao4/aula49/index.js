function cria_pessoa(nome, sobrenome, peso, altura) {
    return {
        nome, 
        sobrenome,
        altura,
        peso,
        get nome_completo() {
            return `${this.nome} ${this.sobrenome}`
        },

        set nome_completo(valor) {
            valor = valor.split(" ")
            this.nome = valor.shift()
        },

        get imc() {
            const imc = this.peso / (this.altura ** 2)
            return imc.toFixed(2)
        },

        fala() {
            return `Olá ${this.nome} ${this.sobrenome}, você pesa ${peso}kg e mede ${altura}m`
        },

    }
}

const pessoa1 = cria_pessoa("Samuel", "Campelo", 65, 1.7)
pessoa1.nome_completo = "Gustavo Guanabara"
console.log(pessoa1.nome_completo)