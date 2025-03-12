function maior_numero(numero1, numero2, numero3) {
    const numeros = [numero1, numero2, numero3]
    let maior = 0

    for (let numero of numeros) {
        if (numero > maior) {
            maior = numero
        }
    }

    return maior
}


console.log(maior_numero(1, 3, 5))