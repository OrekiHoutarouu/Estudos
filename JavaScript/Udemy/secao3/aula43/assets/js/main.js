const relogio = document.querySelector("p#relogio")
let segundos = 0
let cronometro

function criar_cronometro(segundos) {
    const data = new Date(segundos * 1000)
    return data.toLocaleTimeString("pt-BR", {timeZone: "UTC"})
}

function iniciar() {
    clearInterval(cronometro)
    relogio.style.color = "black"

    cronometro = setInterval(function() {
        segundos++
        relogio.innerHTML = criar_cronometro(segundos)
    }, 1000)
}

function pausar() {
    clearInterval(cronometro)
    relogio.style.color = "red"
}

function zerar() {
    clearInterval(cronometro)
    relogio.style.color = "black"

    segundos = 0
    relogio.innerHTML = criar_cronometro(0)
}