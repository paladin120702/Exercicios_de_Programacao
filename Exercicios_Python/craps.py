import random

def jogar_dados():
    return random.randint(1, 6) + random.randint(1, 6)

def craps():
    primeira_jogada = jogar_dados()
    
    if primeira_jogada in [7, 11]:
        return "Natural! Você ganhou!"
    elif primeira_jogada in [2, 3, 12]:
        return "Craps! Você perdeu."
    else:
        ponto = primeira_jogada
        print(f"Ponto é {ponto}")
        
        while True:
            nova_jogada = jogar_dados()
            print(f"Nova jogada: {nova_jogada}")
            
            if nova_jogada == ponto:
                return f"Você tirou o Ponto! Você ganhou!"
            elif nova_jogada == 7:
                return "Você tirou 7. Você perdeu."

resultado = craps()
print(resultado)