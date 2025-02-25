function random(mininmo, maximo) {
    const numero = Math.random() * (maximo - mininmo) + mininmo
    return Math.floor(numero)
}

let numero = random(1, 50)

while (numero !== 10) {
    numero = random(1, 50)
    console.log(numero)
}

do {
    numero = random(1, 50)
    console.log(numero)
} while (numero !== 10)