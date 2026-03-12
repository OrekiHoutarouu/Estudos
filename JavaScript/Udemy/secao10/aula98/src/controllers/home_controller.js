exports.get_home = (requisicao, resposta) => {
    resposta.render("../views/index.ejs")
}

exports.post_home = (requisicao, resposta) => {
    resposta.send(requisicao.body)
}