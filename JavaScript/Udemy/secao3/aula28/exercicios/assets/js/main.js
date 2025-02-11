const titulo = document.querySelector(".container h1")

const data = new Date()
const dia_semana = data.getDay()
const dia_mes = data.getDate()
const mes = data.getMonth()
const ano = data.getFullYear()
const hora = data.getHours()
const minuto = data.getMinutes()

switch(dia_semana) {
    case 0:
        titulo.innerHTML += "Domingo"
        break
    case 1:
        titulo.innerHTML += "Segunda-feira"
        break
    case 2:
        titulo.innerHTML += "Terça-feira"
        break
    case 3:
        titulo.innerHTML += "Quarta-feira"
        break
    case 4:
        titulo.innerHTML += "Quinta-feira"
        break
    case 5:
        titulo.innerHTML += "Sexta-feira"
        break
    case 6:
        titulo.innerHTML += "Sábado"
        break
}

titulo.innerHTML += `, ${dia_mes} de `

switch(mes) {
    case 0:
        titulo.innerHTML += "Janeiro"
        break
    case 1:
        titulo.innerHTML += "Fevereiro"
        break
    case 2:
        titulo.innerHTML += "Março"
        break
    case 3:
        titulo.innerHTML += "Abril"
        break
    case 4:
        titulo.innerHTML += "Maio"
        break
    case 5:
        titulo.innerHTML += "Junho"
        break
    case 6:
        titulo.innerHTML += "Julho"
        break
    case 7:
        titulo.innerHTML += "Agosto"
        break
    case 8:
        titulo.innerHTML += "Setembro"
        break
    case 9:
        titulo.innerHTML += "Outubro"
        break
    case 10:
        titulo.innerHTML += "Novembro"
        break
    case 11:
        titulo.innerHTML += "Dezembro"
        break
}

titulo.innerHTML += ` de ${ano}`
titulo.innerHTML += ` ${hora >= 10 ? hora : `0${hora}`}:${minuto >= 10 ? minuto : `0${minuto}`}`

titulo.innerHTML += "<br> <br>"

titulo.innerHTML += Intl.DateTimeFormat('pt-BR', {dateStyle: "full", timeStyle: "short" }).format(data)