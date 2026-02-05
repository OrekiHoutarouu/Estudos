class Controle_remoto {
    constructor(tv) {
        this.tv = tv
        this.volume = 0
    }

    aumentar_volume() {
        this.volume ++
        console.log(this.volume)
    }

    diminuir_volume() {
        this.volume --
        console.log(this.volume)
    }

    static troca_pilha() {
        console.log("Troquei")
    }
}

const constrole1 = new Controle_remoto("LG")
constrole1.aumentar_volume()
constrole1.aumentar_volume()
constrole1.aumentar_volume()
constrole1.diminuir_volume()
Controle_remoto.troca_pilha()