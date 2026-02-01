const cpf = "070.987.720-03"

function valida_cpf(cpf) {
    const cpf_enviado = limpa_cpf(cpf)

    if (cpf_enviado.length !== 11) return false
    if (verifica_sequencia(cpf_enviado)) return false

    const cpf_novo = faz_contas(Array.from(cpf_enviado))

    return cpf_enviado === cpf_novo
}

function faz_contas(cpf) {
    const cpf_parcial = cpf.slice(0, -2)

    const primeiro_digito = gera_digito(cpf_parcial)
    cpf_parcial.push(String(primeiro_digito))

    const segundo_digito = gera_digito(cpf_parcial)
    cpf_parcial.push(String(segundo_digito))

    const cpf_novo = cpf_parcial

    return cpf_novo.join("")
}

function gera_digito(cpf_parcial) {
    let contador_regressivo = cpf_parcial.length + 1

    const soma_total = cpf_parcial.reduce((acumulador, atual) => {
        acumulador += (contador_regressivo * Number(atual))
        
        contador_regressivo--

        return acumulador
    }, 0)

    const digito = 11 - (soma_total % 11)

    return digito > 9 ? 0 : digito
}

function verifica_sequencia(cpf_enviado){
    const sequencia = cpf_enviado[0].repeat(cpf_enviado.length)
    return sequencia === cpf_enviado
}

function limpa_cpf(cpf) {
    const cpf_limpo = cpf.replace(/\D+/g, "")

    return cpf_limpo
}

console.log(valida_cpf(cpf))