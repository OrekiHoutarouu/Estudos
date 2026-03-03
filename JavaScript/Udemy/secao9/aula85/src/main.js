import Gera_cpf from "./modules/Gera_cpf"
import "./assets/css/style.css"

(function() {
    const cpf = new Gera_cpf()
    const cpf_gerado = document.querySelector("#cpf-gerado")

    cpf_gerado.innerHTML = cpf.gera_novo_cpf()
})()