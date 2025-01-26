let letra1 = "A"
let letra2 = letra1
console.log(letra1, letra2)

letra1 = "B"
console.log(letra1, letra2)

let numero1 = [1, 2, 3]
let numero2 = numero1
console.log(numero1, numero2)

numero1.push(4)
console.log(numero1, numero2)

numero2.pop()
console.log(numero1, numero2)