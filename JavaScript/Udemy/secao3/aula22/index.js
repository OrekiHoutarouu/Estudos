function fala_oi() {
    return "Oi"
}

const vai_executar = "fala"
console.log(vai_executar && fala_oi())

const a = 0
const b = null
const c = "false"
const d = false
const e = NaN

console.log(a || b || c || d || e)