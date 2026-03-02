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

async function executa() {
    try {
        const frase1 = await espera("Frase 1", cria_numero_aleatorio(0, 3))
        console.log(frase1)
        const frase2 = await espera(2, cria_numero_aleatorio(0, 3))
        console.log(frase2)
        const frase3 = await espera("Frase 3", cria_numero_aleatorio(0, 3))
        console.log(frase3)
    } catch {
        console.log("ERRO")
    }

}

executa()