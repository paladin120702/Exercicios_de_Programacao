def multiplicador(multiplicar):
    def vezes(numero):
        return numero * multiplicar
    return vezes    

resultado1 = multiplicador(2)
resultado2 = multiplicador(3)
resultado3 = multiplicador(4)

print(resultado1(2), resultado2(5), resultado3(3))