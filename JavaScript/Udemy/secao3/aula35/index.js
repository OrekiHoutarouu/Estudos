const nomes = ["Samuel", "Campelo"]

for (let valor of nomes) {
    console.log(valor)
}

nomes.forEach(function(elemento, index, array) {
    console.log(index, elemento, array)
});