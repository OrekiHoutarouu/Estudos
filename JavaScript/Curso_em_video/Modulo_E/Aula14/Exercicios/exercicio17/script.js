function gerar_tabuada() {
    var numero = document.getElementById("numero").value
    var tabuada = document.getElementById("tabuada")

    if (numero.length == 0) {
        window.alert("Por favor, digite um número")
    } else {
        numero = Number(numero)

        tabuada.innerHTML = ""
        for (var c = 1; c <= 10; c++) {
            var opcao = document.createElement("option")

            opcao.text = `${numero} x ${c} = ${numero * c}`
            tabuada.appendChild(opcao)
        }
    }
}   