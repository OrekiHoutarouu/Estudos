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

const promises = [
    espera("Frase 1", cria_numero_aleatorio(1, 3)),
    espera("Frase 2", cria_numero_aleatorio(1, 3)),
    espera("Frase 3", cria_numero_aleatorio(1, 3)),
]

Promise.all(promises)
    .then((valor) => {
        console.log(valor)
    })
    .catch((e) => {
        console.log(e)
    })

Promise.race(promises)
    .then((valor) => {
        console.log(valor)
    })
    .catch((e) => {
        console.log(e)
    })

function baixa_pagina() {
    const em_cache = false

    if (em_cache) {
        return Promise.resolve("Página em cache")
    } else {
        return espera("Baixando página", cria_numero_aleatorio(1, 3))
    }
}

baixa_pagina()
    .then(dados => console.log(dados))
    .catch(e => console.log(e))