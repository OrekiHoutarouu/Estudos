class Dispositivo_eletronico {
    constructor(nome) {
        this.nome = nome
        this.ligado = false
    }

    ligar() {
        if (this.ligado) {
            console.log(`${this.nome} ligado.`)
            return
        }

        console.log(`${this.nome} ligado.`)
        this.ligado = true
    }

    desligar() {
        if (!this.ligado) {
            console.log(`${this.nome} desligado`)
            return
        }

        console.log(`${this.nome} desligado.`)
        this.ligado = false
    }
}

class Smartphone extends Dispositivo_eletronico {
    constructor(nome, cor, modelo) {
        super(nome)
        this.cor = cor
        this.modelo = modelo
    }
}

const smartphone1 = new Smartphone("Iphone", "Preto", "17 Pro Max")
console.log(smartphone1)
smartphone1.ligar()
smartphone1.desligar()

class Tablet extends Dispositivo_eletronico {
    constructor(nome, wifi) {
        super(nome)
        this.wifi = wifi
    }
}

const tablet1 = new Tablet("Multilaser", true)

console.log(tablet1)