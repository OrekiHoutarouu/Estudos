const nomes = ["Samuel", "Campelo", "Maria", "João", "Gabriel", "Julia"]
const removidos = nomes.splice(4, 2)

console.log(nomes, removidos)

const nomes2 = ["Samuel", "Campelo", "Maria", "João", "Gabriel", "Julia"]
nomes2.splice(3, 1, "Luís")

console.log(nomes2)