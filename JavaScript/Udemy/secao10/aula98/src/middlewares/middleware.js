exports.middleware_global = (requisicao, res, next) => {
    console.log()
    console.log(requisicao.body)
    console.log()

    next()
}