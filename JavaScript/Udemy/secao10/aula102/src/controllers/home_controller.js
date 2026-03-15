exports.get_home = (request, answer) => {
    answer.render("../views/index.ejs", {
        title: "Home title",
    })
}

exports.post_home = (request, answer) => {
    answer.send(request.body)
}

