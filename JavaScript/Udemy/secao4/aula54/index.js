function* geradora() {
    yield "valor 1"
    yield "valor 2"
    yield "valor 3"
}

let teste = geradora()
for (let valor of teste) {
    console.log(valor)
}

function* geradora2() {
    yield 0
    yield 1
    yield 2
}

function* geradora3() {
    yield* geradora2()
    yield 3
    yield 4
    yield 5
}

let teste2 = geradora3() 
for (let valor of teste2) {
    console.log(valor)
}