function Conta(agencia, conta, saldo) {
    this.agencia = agencia
    this.conta = conta
    this.saldo = saldo
}

Conta.prototype.sacar = function(valor) {
    if (this.saldo < valor) {
        console.log("Saldo insuficiente")
        this.ver_saldo()
        return
    }

    this.saldo -= valor
    this.ver_saldo()
}

Conta.prototype.depositar = function(valor) {
    this.saldo += valor
    this.ver_saldo()
}

Conta.prototype.ver_saldo = function() {
    console.log(`Agência: ${this.agencia}`)
    console.log(`Conta: ${this.conta}`)
    console.log(`Você tem R$${this.saldo}`)
}


function Conta_corrente(agencia, conta, saldo, limite) {
    Conta.call(this, agencia, conta, saldo)
    this.limite = limite
}

Conta_corrente.prototype = Object.create(Conta.prototype)
Conta_corrente.prototype.constructor = Conta_corrente

Conta_corrente.prototype.sacar = function(valor) {
    if ((this.saldo + this.limite) < valor) {
        console.log("Saldo insuficiente")
        this.ver_saldo()
        return
    }

    this.saldo -= valor
    this.ver_saldo()
}


function Conta_poupanca(agencia, conta, saldo) {
    Conta.call(this, agencia, conta, saldo)
}

Conta_poupanca.prototype = Object.create(Conta.prototype)
Conta_poupanca.prototype.constructor = Conta_poupanca


const conta_corrente = new Conta_corrente(11, 22, 0, 100)
const conta_poupanca = new Conta_poupanca(33, 44, 10)

conta_corrente.sacar(50)
conta_poupanca.depositar(10)
conta_poupanca.sacar(15)