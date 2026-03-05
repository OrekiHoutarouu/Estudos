const cria_numero_aleatorio = (min, max) => Math.floor(Math.random() * (max - min) + min)
const gera_maiuscula = () => String.fromCharCode(cria_numero_aleatorio(65, 91))
const gera_minuscula = () => String.fromCharCode(cria_numero_aleatorio(97, 123))
const gera_numero = () => String.fromCharCode(cria_numero_aleatorio(48, 58))
const simbolos = "!@#$%&*()+-/?_{}[]"
const gera_simbolo = () => simbolos[cria_numero_aleatorio(0, simbolos.length)]

export default function gera_senha(quantidade, maiusculas, minusculas, numeros, simbolos) {
    const senha = []
    quantidade = Number(quantidade)

    for (let i = 0; i < quantidade; i++) {
        maiusculas && senha.push(gera_maiuscula())
        minusculas && senha.push(gera_minuscula())
        numeros && senha.push(gera_numero())
        simbolos && senha.push(gera_simbolo())
    }

    return senha.join("").slice(0, quantidade)
}