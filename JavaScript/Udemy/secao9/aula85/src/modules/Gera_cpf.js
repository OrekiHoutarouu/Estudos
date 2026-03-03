import Valida_cpf from "./Valida_cpf";

export default class Gera_cpf {

    random(min = 100000000, max = 999999999) {
        return String(Math.floor(Math.random() * (max - min) + min))
    }

    formata_cpf(cpf) {
        return (
            cpf.slice(0, 3) + "." +
            cpf.slice(3, 6) + "." +
            cpf.slice(6, 9) + "-" +
            cpf.slice(9, 11)
        )
    }

    gera_novo_cpf() {
        const cpf_sem_digito = this.random()
        const digito1 = Valida_cpf.gera_digito(cpf_sem_digito)
        const digito2 = Valida_cpf.gera_digito(cpf_sem_digito + digito1)

        const novo_cpf = cpf_sem_digito + digito1 + digito2

        return this.formata_cpf(novo_cpf)
    }
}