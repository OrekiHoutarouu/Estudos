function retorna_hora(data) {
    if (data && !(data instanceof Date)) {
        throw new TypeError("Esperando instância de Date.")
    }

    if(!data) {
        data = new Date()
    }

    return data.toLocaleTimeString("pt-BR")
}

try {
    var hora = retorna_hora(new Date)
} catch(erro) {
    hora = "Não encontrada"
} finally {
    console.log(`Hora: ${hora}. Tenha um bom dia.`)
}