function funcao1(callback) {
    setTimeout(function() {
        console.log("funcao1")
        if (callback) callback()
    }, 500)
}

function funcao2(callback) {
     setTimeout(function() {
        console.log("funcao2")
        if (callback) callback()
    }, 1000)
}

function funcao3(callback) {
     setTimeout(function() {
        console.log("funcao3")
        if (callback) callback()
    }, 800)
}

funcao1(funcao1_callback)

function funcao1_callback() {
    funcao2(funcao2_callback)
}

function funcao2_callback() {
    funcao3(funcao3_callback)
}

function funcao3_callback() {
    console.log("Olá mundo!")
}