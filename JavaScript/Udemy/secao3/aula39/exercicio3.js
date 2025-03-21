function fizz_buzz(numero) {
    if (isNaN(numero)) {
        return numero
    } else if (numero < 0 || numero > 100) {
        return
    }

    if (numero % 3 === 0 && numero % 5 === 0) {
        return "FizzBuzz"
    } else if (numero % 3 !== 0 && numero % 5 !== 0) {
        return numero
    } else if (numero % 3 === 0 ) {
        return "Fizz"
    } else if (numero % 5 === 0) {
        return "Buzz"
    }
}

for (let i = 0; i < 100; i++) {
    let fizz_ou_buzz = fizz_buzz(i)
    console.log(fizz_ou_buzz)
}