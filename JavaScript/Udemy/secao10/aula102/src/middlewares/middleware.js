exports.middleware_global = (requisicao, resposta, next) => {   
    next()
}

exports.check_csrf_error = (erro, requisicao, resposta, next) => {
    if (erro && erro.code === "EBADCSRFTOKEN") {
        return resposta.render("../views/includes/404", {
            titulo: "ERRO"
        })
    }
}

exports.csrf_middleware = (requisicao, resposta, next) => {
    resposta.locals.csrfToken = requisicao.csrfToken()
    next()
}