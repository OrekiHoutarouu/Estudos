const cor_secundaria = "#58A4B0"
const cor_terciaria = "#8C271E"

function calcula_imc() {
    const peso = Number(document.querySelector("#peso").value)
    const altura = Number(document.querySelector("#altura").value)

    const imc = peso / altura ** 2

    mostra_imc(peso, altura, imc)
}

function mostra_imc(peso, altura, imc) {
    const resultado = document.querySelector("#resultado-imc")
    resultado.style.padding = "10px"

    if (peso == 0) {
        resultado.innerHTML = `Peso inválido`
        resultado.style.background = cor_terciaria
    } else if (altura == 0) {
        resultado.innerHTML = `Altura inválida`
        resultado.style.background = cor_terciaria
    } else if (imc < 18.5) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Abaixo do peso)`;
        resultado.style.background = cor_secundaria
    } else if (imc >= 18.5 && imc < 25) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Peso normal)`;
        resultado.style.background = cor_secundaria
    } else if (imc >= 25 && imc < 30) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Sobrepeso)`;
        resultado.style.background = cor_secundaria
    } else if (imc >= 30 && imc < 35) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Obesidade grau 1)`;
        resultado.style.background = cor_secundaria
    } else if (imc >= 35 && imc < 40) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Obesidade grau 2)`;
        resultado.style.background = cor_secundaria
    } else if (imc > 40) {
        resultado.innerHTML = `Seu IMC é de ${imc.toFixed(2)} (Obesidade grau 3)`;
        resultado.style.background = cor_secundaria
    }
}