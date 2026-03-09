const express = require("express")
const app = express() 

app.get("/", (requisicao, resposta) => {
    resposta.send(`
        <form action="/" method="POST">
            <label for="nome">Nome:</label>
            <input type="text" name="nome">
            
            <button type="submit">Enviar</button>
        </form>
        `)
})

app.get("/testes/:idUsuario", (requisicao, resposta) => {
    console.log(requisicao.params)
    console.log(requisicao.query)
    resposta.send("Oi")
})

app.post("/", (requisicao, resposta) => {
    resposta.send("Recebi o formulário")
})

app.listen(3000, () => {
    console.log("Servidor executando na porta 3000")
    console.log("http://localhost:3000/")
})