for (let c = 0; c < 10; c++) {
    console.log(c)
}

for (let c = 500; c > 400; c -= 10) {
    console.log(c)
}

for (let c = 1; c < 10; c++){
    const par_impar = c % 2 === 0 ? "Par" : "Ímpar"
    console.log(c, par_impar)
}

const frutas = ["Maçã", "Pêra", "Uva"]

for (let c = 0; c < frutas.length; c++) {
    console.log(c, frutas[c])
}