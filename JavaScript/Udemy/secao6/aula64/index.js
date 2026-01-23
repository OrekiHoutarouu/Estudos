const produto = {nome: "Caneca", preco: 5}
const caneca = {
    ...produto,
    material: "Porcelana"
}

const caneca2 = Object.assign({}, produto, {material: "Plástico"})


console.log(produto)
console.log(caneca)
console.log(caneca2)