const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
const [primeiroNumero, segundoNumero, ...resto] = numeros
console.log(primeiroNumero, segundoNumero, resto)  

const variosNumeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
console.log(variosNumeros[0][0])