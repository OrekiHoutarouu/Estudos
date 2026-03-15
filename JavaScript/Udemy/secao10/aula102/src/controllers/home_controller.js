exports.get_home = (requisicao, resposta) => {
    resposta.render("../views/index.ejs", {
        titulo: "Título da home",
    })
}

exports.post_home = (requisicao, resposta) => {
    resposta.send(requisicao.body)
}

