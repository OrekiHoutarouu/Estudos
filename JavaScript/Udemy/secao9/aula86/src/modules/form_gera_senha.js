import gera_senha from "./geradores";

const senha_gerada = document.querySelector("#senha-gerada")
const caracteres = document.querySelector("#caracteres")
const maiusculas = document.querySelector("#maiusculas")
const minusculas = document.querySelector("#minusculas")
const numeros = document.querySelector("#numeros")
const simbolos = document.querySelector("#simbolos")
const gerar_senha = document.querySelector("#gerar-senha")

export default () => {
    gerar_senha.addEventListener("click", (e) => {
        e.preventDefault()
        senha_gerada.innerHTML = gera()
    })
}

function gera() {
    const senha = gera_senha(
        caracteres.value, 
        maiusculas.checked,
        minusculas.checked,
        numeros.checked,
        simbolos.checked
    )

    return senha || "Nada selecionado"
}