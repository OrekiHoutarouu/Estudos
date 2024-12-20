function testa_numero(numero) {
    if (Number(numero) >= 1 && Number(numero) <= 100) {
        return true
    } else {
        return false
    }
}

function testa_lista(numero, lista) {
    if (lista.indexOf(Number(numero)) != -1) {
        return true
    } else {
        return false
    }
}

function adicionar() {
    let numero = document.getElementById("numero").value
    let lista = document.getElementById("lista")
    let resultado = document.getElementById("resultado")
    let valores = []
    
    if (testa_numero(numero) && !testa_lista(numero, valores)) {
        window.alert("Tudo ok")
    } else {
        window.alert("Valor inválido ou já encontrado na lista.")
    }
}
