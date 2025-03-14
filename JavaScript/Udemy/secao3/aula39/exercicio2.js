function e_paisagem(largura, altura) {
    return largura > altura
}

if (e_paisagem(30, 20)) {
    console.log("Está no modo paisagem")
} else {
    console.log("Está no modo retrato")
}