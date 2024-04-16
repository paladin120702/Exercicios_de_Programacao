'''
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4
'''
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def soma(n1, n2, d1, d2):
    s1 = n1 * d2
    s2 = n2 * d1
    resultado1 = s1 + s2
    resultado2 = d1 * d2
    divisor = mdc(resultado1, resultado2)
    simplificador_numerador = resultado1 // divisor
    simplificador_denominador = resultado2 // divisor
    return f'{resultado1}/{resultado2} = {simplificador_numerador}/{simplificador_denominador}'

def Subtração(n1, n2, d1, d2):
    s1 = n1 * d2
    s2 = n2 * d1
    resultado1 = s1 - s2
    resultado2 = d1 * d2
    divisor = mdc(resultado1, resultado2)
    simplificador_numerador = resultado1 // divisor
    simplificador_denominador = resultado2 // divisor
    return f'{resultado1}/{resultado2} = {simplificador_numerador}/{simplificador_denominador}'

def Multiplicação(n1, n2, d1, d2):
    m1 = n1 * n2
    m2 = d1 * d2
    divisor = mdc(m1, m2)
    simplificador_numerador = m1 // divisor
    simplificador_denominador = m2 // divisor
    return f'{m1}/{m2} = {simplificador_numerador}/{simplificador_denominador}'

def Divisão(n1, n2, d1, d2):
    di1 = n1 * d2
    di2 = n2 * d1
    divisor = mdc(di1, di2)
    simplificador_numerador = di1 // divisor
    simplificador_denominador = di2 // divisor
    return f'{di1}/{di2} = {simplificador_numerador}/{simplificador_denominador}'


print (soma(1, 3, 2, 4))
print (Subtração(1, 3, 2, 4))
print (Multiplicação(2, 6, 3, 6))
print (Divisão(1, 3, 2, 4))


