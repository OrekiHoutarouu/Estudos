class Valida_formulario {
    constructor() {
        this.formulario = document.querySelector(".formulario")
        
        this.eventos()
    }

    eventos() {
        this.formulario.addEventListener("submit", e => {
            this.handle_submit(e)
        })
    }

    handle_submit(e) {
        e.preventDefault()

        const campos_validos = this.verifica_campos()
        const senhas_validas = this.verifica_senhas()

        if (campos_validos && senhas_validas) {
            alert("Formulário enviado")
            this.formulario.submit()
        }
    }

    verifica_senhas() {
        let valido = true

        const senha = this.formulario.querySelector(".senha")
        const repetir_senha = this.formulario.querySelector(".repetir-senha")

        if (senha.value !== repetir_senha.value) {
            valido = false

            this.cria_erro(senha, "Campos senha e repetir senha precisam ser iguais")
            this.cria_erro(repetir_senha, "Campos senha e repetir senha precisam ser iguais")
        }

        if (senha.value.length < 6 || senha.value.length > 12) {
            valido = false

            this.cria_erro(senha, "Senha deve ter entre 3 e 12 caracteres")
        }

        return valido
    }

    verifica_campos() {
        let valido = true

        for (let texto_erro of this.formulario.querySelectorAll(".mensagem-erro")) {
            texto_erro.remove()
        }

        for (let campo of this.formulario.querySelectorAll(".validar")) {
            if (!campo.value) {
                this.cria_erro(campo, `O campo ${campo.previousElementSibling.innerText} não pode estar em branco`)
                valido = false
            }

            if (campo.classList.contains("cpf")) {
                if (!this.valida_CPF(campo)) valido = false
            }

            if (campo.classList.contains("usuario")) {
                if (!this.valida_usuario(campo)) valido = false
            }
        }

        return valido
    }

    valida_CPF(campo) {
        const cpf = new Valida_cpf(campo.value)

        if (!cpf.valida_cpf()) {
            this.cria_erro(campo, "CPF inválido")
            return false
        }

        return true
    }

    valida_usuario(campo) {
        const usuario = campo.value
        let valido = true

        if (usuario.length < 3 || usuario.length > 12) {
            this.cria_erro(campo, "Usuário deve ter entre 3 e 12 caracteres")
            valido = false
        }

        if (!usuario.match(/^[a-zA-Z0-9]+$/g)) {
            this.cria_erro(campo, "Usuário deve conter apenas letras e/ou números")
            valido = false
        }
        
        return valido
    }

    cria_erro(campo, mensagem) {
        const div = document.createElement("div")

        div.innerHTML = mensagem

        div.classList.add("mensagem-erro")
        campo.insertAdjacentElement("afterend", div)
    }
}   

const valida = new Valida_formulario()