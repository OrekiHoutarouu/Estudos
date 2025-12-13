function funcao(primeiro, segundo, terceiro) {
    let total = 0

    for(let argumento of arguments) {
        total += argumento
    }

    console.log(total, primeiro, segundo, terceiro)
}

funcao(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

function segunda_funcao(a, b, c, d, e, f) {
    console.log(a, b, c, d, e, f)
}

segunda_funcao(1, 2, 3)

function terceira_funcao(a, b = 2) {
    console.log(a + b)
}

terceira_funcao(2)

function quarta_funcao({nome, sobrenome, idade}) {
    console.log(nome, sobrenome, idade)
}

quarta_funcao({nome: "Samuel", sobrenome: "Campelo", idade: 16})

function quinta_funcao([valor1, valor2, valor3]) {
    console.log(valor1, valor2, valor3)
}

quinta_funcao(["Samuel", "Campelo", 16])

function conta(operador, acumulador, ...numeros) {
    for(let numero of numeros) {
        if (operador === "+") acumulador += numero
        else if (operador === "-") acumulador -= numero
        else if (operador === "/") acumulador /= numero
        else if (operador === "*") acumulador *= numero
    }

    console.log(acumulador)
}

conta("-", 10, 40)

