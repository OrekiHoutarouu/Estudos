function carregar() {
    var mensagem = window.document.getElementById("mensagem")
    var imagem = window.document.getElementById("imagem")
    var hora = (new Date()).getHours() + ":" + (new Date()).getMinutes()

    if (hora >= 0 && hora <= 11) {
        imagem.src = "imagens/manha.jpg"
        document.body.style.background = "#7696a5"

    } else if (hora >= 12 && hora <= 17) {
        imagem.src = "imagens/tarde.jpg"
        document.body.style.background = "#c9641f"

    } else {
        imagem.src = "imagens/noite.jpg"
        document.body.style.background = "#303133"
    }

    mensagem.innerHTML = `Agora são ${hora} horas`
}