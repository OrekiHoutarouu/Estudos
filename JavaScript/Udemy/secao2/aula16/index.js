function saudacao(nome) {
    return `Olá, ${nome}!`
} 

console.log(saudacao("Samuel"))

function soma(numero1 = 0, numero2 = 0) {
    const resultado = numero1 + numero2
    return resultado
}

console.log(soma(2, 2))

const quadrado = function(numero) {
    return numero ** 2
}
console.log(quadrado(3))

const raiz = numero => numero ** 0.5
console.log(raiz(9))