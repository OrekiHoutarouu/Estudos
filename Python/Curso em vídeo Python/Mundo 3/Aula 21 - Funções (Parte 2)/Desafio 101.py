def voto(anoDeNascimento):
    from datetime import datetime
    
    idade = datetime.now().year - anoDeNascimento 
    
    if idade < 16:
        return f'Com {idade} anos: Voto negado'
        
    elif idade >= 16 and idade <= 17:
        return f'Com {idade} anos: Voto opcional'
        
    elif idade >= 18 and idade <= 70:
        return f'Com {idade} anos: Voto obrigatório'
    
    elif idade > 70:
        return f'Com {idade} anos: Voto opcional'


anoDeNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoDeNascimento))