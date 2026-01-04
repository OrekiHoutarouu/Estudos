function cria_calculadora() {
    return {
        display: document.querySelector(".display"),

        inicia() {
            this.clique_botoes()
        },

        clique_botoes() {
            document.addEventListener("click", (e) => {
                const el = e.target
                
                if (el.classList.contains("btn-num")) {
                    this.btn_para_display(el.innerText)
                } else if (el.classList.contains("btn-clear")) {
                    this.limpa_display()
                } else if (el.classList.contains("btn-del")) {
                    this.deleta_caractere()
                } else if (el.classList.contains("btn-eq")) {
                    this.realiza_conta()
                }
            })
        },
        
        btn_para_display(valor) {
            this.display.value += valor
        },

        limpa_display() {
            this.display.value = ""
        },

        deleta_caractere() {
            this.display.value = this.display.value.slice(0, -1)
        },

        realiza_conta() {
            let conta = this.display.value

            try {
                conta = eval(conta)

                if(!conta) {
                    alert("Conta inválida")
                    return
                }

                this.display.value = conta
            } catch(e) {
                alert("Conta inválida")
                return
            }
        }
    }
}

const calculadora = cria_calculadora()
calculadora.clique_botoes()