exports.get_home = (requisicao, resposta) => {
    resposta.send(`
        <form action="/" method="POST">
            <label for="nome">Nome:</label>
            <input type="text" name="nome">
            
            <button type="submit">Enviar</button>
        </form>
        `
    )
}

exports.post_home = (requisicao, resposta) => {
    resposta.send("Formulário enviado")
}