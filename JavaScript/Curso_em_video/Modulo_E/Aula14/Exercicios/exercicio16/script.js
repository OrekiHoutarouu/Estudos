function contar() {
    var inicio = (document.getElementById("inicio")).value
    var fim = (document.getElementById("fim")).value
    var passo = (document.getElementById("passo")).value
    var resultado = document.getElementById("resultado")

    if (inicio.length == 0 || fim.length == 0 || passo.length == 0 || Number(passo) <= 0) {
        resultado.innerHTML = "Impossível contar"
        window.alert("Faltam dados")
    } else {
        inicio = Number(inicio)
        fim = Number(fim)
        passo = Number(passo)
        resultado.innerHTML = "Contando: <br>"

        if (inicio < fim) {
            for (let c = inicio; c <= fim; c += passo) {
                resultado.innerHTML += `${c} \u{27A1}`
            }
        } else {
            for (let c = inicio; c >= fim; c -= passo) {
                resultado.innerHTML += `${c} \u{27A1}`
            }
        }
        resultado.innerHTML += `\u{1F3C1}`
    }
}