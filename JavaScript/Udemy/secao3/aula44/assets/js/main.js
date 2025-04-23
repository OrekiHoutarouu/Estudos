const input_tarefa = document.querySelector("input#input_tarefa")
const tarefas = document.querySelector("ul#tarefas")

input_tarefa.addEventListener("keypress", function(e) {
    if (e.keyCode === 13) {
        e.preventDefault()
        adicionar_tarefa()
    }
})

function criar_botao_apagar(item) {
    const botao = document.createElement("input")
    botao.type = "button"
    botao.value = "Apagar"
    botao.setAttribute("class", "apagar")

    item.appendChild(botao)
}

function limpar_input() {
    input_tarefa.value = ""
    input_tarefa.focus()
}

function adicionar_tarefa() {
    if (!input_tarefa.value) {
        return
    }

    const item = document.createElement("li")

    item.innerText = input_tarefa.value

    tarefas.appendChild(item)
    limpar_input()
    criar_botao_apagar(item)
    salvar_tarefas()
}

function salvar_tarefas() {
    const elementos = tarefas.querySelectorAll("li")
    const lista_tarefas = []

    for (let tarefa of elementos) {
        lista_tarefas.push(tarefa.innerText)
    }

    const tarefasJSON = JSON.stringify(lista_tarefas)
    localStorage.setItem("JSON_de_tarefas", tarefasJSON)
}

document.addEventListener("click", function(e) {
    const elemento = e.target

    if (elemento.classList.contains("apagar")) {
        elemento.parentElement.remove()
        salvar_tarefas()
    }
})

function adicionar_tarefas_salvas() {
    const JSON_de_tarefas = localStorage.getItem("JSON_de_tarefas")
    const lista_tarefas = JSON.parse(JSON_de_tarefas)
    
    for (let tarefa of lista_tarefas) {
        const item = document.createElement("li")

        item.innerText = tarefa

        tarefas.appendChild(item)
        criar_botao_apagar(item)
        salvar_tarefas()
    }
}

adicionar_tarefas_salvas()