const nome = "Samuel Campelo"
console.log(nome[0])

const alunos = ["Samuel", "Luiz", "Maria"]
console.log(alunos[1])
console.log(alunos.length)

alunos[1] = "Eduardo"
console.log(alunos)

alunos.push("João")
console.log(alunos)

alunos.pop()
console.log(alunos)

alunos.unshift("Luiza")
console.log(alunos)

alunos.shift()
console.log(alunos)

console.log(alunos.slice(0, 2))