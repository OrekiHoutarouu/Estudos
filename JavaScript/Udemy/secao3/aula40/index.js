try {
    console.log(nao_existo)
} catch(erro) {
    console.log("Não existe essa variável")
    console.log(erro)
}

function soma(x, y) {
    if (typeof x !== "number" || typeof y !== "number") {
        throw new Error("x e y precisam ser números.")
    }

    return x + y
}

try {
    console.log(soma(2, 3))
    console.log(soma(1, "3"))
} catch(erro) {
    console.log("x e y precisam ser números.")
}