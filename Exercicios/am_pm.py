def hora(a):
    if a >= 12:
        calculo = a - 12
        resultado = print (f'{calculo:.2f} AM')
        return resultado
        
    if a <= 11.59:
        calculo2 = a + 12
        resultado2 = print (f'{calculo2:.2f} PM')
        return resultado2
        
hora(float(input('Digite a hora ')))