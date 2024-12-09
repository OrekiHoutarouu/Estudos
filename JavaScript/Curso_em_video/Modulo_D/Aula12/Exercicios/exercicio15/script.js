function verificar() {
    var ano = (new Date()).getFullYear()
    var ano_nascimento = document.getElementById("ano_nascimento").value
    var resultado = document.getElementById("resultado")
    
    if (ano_nascimento.length == 0 || ano_nascimento > ano) {
        window.alert("Verifique os dados e tente novamente")
    } else {
        var imagem = document.createElement("img")
        imagem.setAttribute("id", "imagem")

        var idade = ano - ano_nascimento
        var sexo = ""
        
        if (document.getElementsByName("sexo")[0].checked) {
            sexo = "Homem"

            switch(idade) {
                case idade <= 12:
                    imagem.setAttribute("src", "imagens/bebe_homem.jpg")
                    break

                case idade >= 13 && idade <= 21:
                    imagem.setAttribute("src", "imagens/jovem_homem.jpg")
                    break
                
                case idade >= 22 && idade <= 59:
                    imagem.setAttribute("src", "imagens/adulto_homem.jpg")
                    break
                
                case idade >= 60:
                    imagem.setAttribute("src", "imagens/idoso_homem.jpg")
                    break
            }
        } else {
            sexo = "Mulher"

            switch(idade) {
                case idade <= 12:
                    imagem.setAttribute("src", "imagens/bebe_mulher.jpg")
                    break

                case idade >= 13 && idade <= 21:
                    imagem.setAttribute("src", "imagens/jovem_mulher.jpg")
                    break
                
                case idade >= 22 && idade <= 59:
                    imagem.setAttribute("src", "imagens/adulta_mulher.jpg")
                    break
                
                case idade >= 60:
                    imagem.setAttribute("src", "imagens/idosa_mulher.jpg")
                    break
            }
        }

        resultado.innerText = `Detectamos ${sexo} com ${idade} anos.`
        resultado.appendChild(imagem)
    }

}