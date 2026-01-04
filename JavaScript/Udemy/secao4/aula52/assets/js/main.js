function Calculadora() {
    this.display = document.querySelector(".display");

    this.inicia = function() {
        this.clique_botoes()
    }

    this.clique_botoes = function() {
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
    }
    
    this.btn_para_display = function(valor) {
        this.display.value += valor
    }

    this.limpa_display = function() {
        this.display.value = ""
    }

    this.deleta_caractere = function() {
        this.display.value = this.display.value.slice(0, -1)
    }

    this.realiza_conta = function() {
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

const calculadora = new Calculadora()
calculadora.clique_botoes()

