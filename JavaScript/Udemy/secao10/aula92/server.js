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

app.post("/", (requisicao, resposta) => {
    resposta.send("Recebi o formulário")
})

app.get("/contato", (requisicao, resposta) => {
    resposta.send("Obrigado por entrar em contato conosco")
})

app.listen(3000, () => {
    console.log("Servidor executando na porta 3000")
    console.log("http://localhost:3000/")
})