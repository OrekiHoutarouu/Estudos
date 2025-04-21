function pegar_hora_atual() {
    let data = new Date()

    return data.toLocaleTimeString("pt-BR")
}

const timer = setInterval(function() {console.log(pegar_hora_atual())}, 1000)

setTimeout(function() {clearInterval(timer)}, 10000)