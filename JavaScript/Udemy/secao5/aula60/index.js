const numeros = [5, 50, 80, 1, 2, 3, 5, 8, 7, 11, 15, 22, 27]

const pares = numeros.filter(valor => valor % 2 === 0)
console.log(pares)

const dobro_pares = pares.map(valor => valor * 2)
console.log(dobro_pares)

const soma_dobros = dobro_pares.reduce((acumulador, valor) => acumulador += valor)
console.log(soma_dobros)