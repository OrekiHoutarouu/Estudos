function soma(a, b) {
    return a + b
}

let resultado = soma(2, 5)
console.log(resultado)

function cria_pessoa(nome, sobrenome) {
    return {nome, sobrenome}
}

const pessoa1 = cria_pessoa("Samuel", "Campelo")
console.log(pessoa1)

function fala_comeco_frase(comeco){
    function fala_final_frase(final){
        return `${comeco} ${final}`
    }
    return fala_final_frase
}

const comeco = fala_comeco_frase("Olá")
const final = comeco("Mundo")
console.log(final)

function pega_primeiro_termo(x) {
  function soma_primeiro_termo_com_segundo_termo(y) {
    return x + y
  }
  return soma_primeiro_termo_com_segundo_termo 
}

primeiro_termo = pega_primeiro_termo(2)
soma = primeiro_termo(3)
console.log(soma)