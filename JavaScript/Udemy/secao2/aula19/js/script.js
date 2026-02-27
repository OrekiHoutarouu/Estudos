function main() {
    const formulario = document.querySelector(".formulario")
    const resultado = document.querySelector(".resultado")
    const pessoas = []

    function recebe_evento(evento) {
        evento.preventDefault()

        const nome = formulario.querySelector(".nome")
        const sobrenome = formulario.querySelector(".sobrenome")
        const peso = formulario.querySelector(".peso")
        const altura = formulario.querySelector(".altura")

        const pessoa = {
            nome : nome.value,
            sobrenome: sobrenome.value,
            peso : peso.value,
            altura : altura.value
        }

        pessoas.push(pessoa)
        resultado.innerHTML += `${nome.value} ${sobrenome.value} ${(peso.value)}Kg ${altura.value}m <br>`
    }

    formulario.addEventListener("submit", recebe_evento)
}

main()