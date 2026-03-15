exports.global_middleware = (request, answer, next) => {   
    next()
}

exports.check_csrf_error = (error, request, answer, next) => {
    if (error && error.code === "EBADCSRFTOKEN") {
        return answer.render("../views/includes/404", {
            title: "ERROR"
        })
    }
}

exports.csrf_middleware = (request, answer, next) => {
    answer.locals.csrfToken = request.csrfToken()
    next()
}