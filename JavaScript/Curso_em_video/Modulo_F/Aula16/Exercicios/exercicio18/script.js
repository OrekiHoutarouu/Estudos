let valores = []

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
    
    if (testa_numero(numero) && !testa_lista(numero, valores)) {
        let resultado = document.getElementById("resultado")
        valores.push(Number(numero))
        
        let item = document.createElement("option")
        lista.appendChild(item)
        resultado.innerHTML = ""

        item.text = `Valor ${numero} adicionado.`
    } else {
        window.alert("Valor inválido ou já encontrado na lista.")
    }
}

function finalizar() {
    if (valores.length == 0) {
        window.alert("Adicione valores antes de finalizar")
    } else { 
        let total_valores = valores.length
        let maior_valor = valores[0]
        let menor_valor = valores[0]
        let soma = 0
        let media = 0

        for (let posicao in valores) {
            soma += valores[posicao]

            if (valores[posicao] > maior_valor) {
                maior_valor = valores[posicao]
            }

            if (valores[posicao] < menor_valor) {
                menor_valor = valores[posicao]
            }
        }

        media = soma / total_valores

        resultado.innerHTML = ""
        resultado.innerHTML += `<p>Ao todo, temos ${total_valores} valores cadastrados</p>`
        resultado.innerHTML += `<p>O maior valor cadastrado foi ${maior_valor}</p>`
        resultado.innerHTML += `<p>O menor valor cadastrado foi ${menor_valor}</p>`
        resultado.innerHTML += `<p>A soma de todos os valores é igual a ${soma}</p>`
        resultado.innerHTML += `<p>A média de todos os valores é igual a ${media}</p>`
    }
}
