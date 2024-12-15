let valores = [8, 1, 7, 4, 2, 9]

console.log("Antes de colocar em ordem: ")

for (let valor = 0; valor < valores.length; valor++) {
    console.log(`A posição ${valor} tem valor ${valores[valor]}`)
}

valores.sort()
console.log("Após colocar em ordem: ")

for (let valor in valores) {
    console.log(`A posição ${valor} tem valor ${valores[valor]}`)
}

console.log(`O valor 8 está na posição ${valores.indexOf(8)}`)