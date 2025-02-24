const div_paragrafos = document.querySelector(".paragrafos")
const paragrafos = document.querySelectorAll("p")

const estilos_body = getComputedStyle(document.body)
const background_color_body = estilos_body.backgroundColor

for (let paragrafo of paragrafos) {
    paragrafo.style.backgroundColor = background_color_body
    paragrafo.style.color = "#FFFFFF"
}