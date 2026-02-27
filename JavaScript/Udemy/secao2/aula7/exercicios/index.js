const nome = "Samuel Luís"
const sobrenome = "Vital Campelo"
const idade = 15
const peso = 65
const altura = 1.70
let indiceMassaCorporal = peso / (altura**2)
let anoNascimento = ((new Date).getFullYear()) - idade

console.log(`${nome} ${sobrenome} tem ${idade} anos, pesa ${peso}kg`)
console.log(`tem ${altura}m de altura e seu IMC é de ${indiceMassaCorporal}`)
console.log(`${nome} nasceu em ${anoNascimento}`)