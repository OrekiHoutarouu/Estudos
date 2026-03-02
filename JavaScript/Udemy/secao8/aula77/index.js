function cria_numero_aleatorio(min, max) {
    max *= 1000
    min *= 1000

    return Math.floor(Math.random() * (max - min) + min)
}

function espera(mensagem, tempo) {
    return new Promise((resolve, reject) => {
        if (typeof mensagem !== "string") reject("ERRO")

        setTimeout(() => {
            resolve(mensagem)
        }, tempo) 
    })
}

espera("Frase 1", cria_numero_aleatorio(1, 3))
    .then(resposta => {
        console.log(resposta)
        return espera("Frase 2", cria_numero_aleatorio(1, 3))
    })
    .then(resposta => {
        console.log(resposta)
        return espera(1, cria_numero_aleatorio(1, 3))
    })
    .then(resposta => {
        console.log(resposta)
    })
    .catch(e => {
        console.log(e)
    })

console.log("Isso será executado primeiro")