document.addEventListener("click", e => {
    const element = e.target
    const tag = element.tagName.toLowerCase()

    if (tag === "a") {
        e.preventDefault()

        carrega_pagina(element)
    }
})

async function carrega_pagina(elemento) {
    const href = elemento.getAttribute("href")

    try {
        const response = await fetch(href)
        if (response.status !== 200) throw new Error("ERRO")
        const html = await response.text()
    
        carrega_resultado(html)
    } catch(e) {
        console.log(e)
    }
}

function carrega_resultado(response) {
    const resultado = document.querySelector("#resultado")

    resultado.innerHTML = response
}