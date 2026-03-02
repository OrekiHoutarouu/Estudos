const request = objeto => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest()
    
        xhr.open(objeto.method, objeto.url, true)
        xhr.send()
    
        xhr.addEventListener("load", () => {
            if(xhr.status >= 200 && xhr.status < 300) {
                resolve(xhr.responseText)
            } else {
                reject(xhr.statusText)
            }
        })
    })

}

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
    
    const config_objeto = ({
        method: "GET",
        url: href,
    })

    try {
        const response = await request(config_objeto)
        carrega_resultado(response)
    } catch(e) {
        console.log(e)
    }
}

function carrega_resultado(response) {
    const resultado = document.querySelector("#resultado")

    resultado.innerHTML = response
}