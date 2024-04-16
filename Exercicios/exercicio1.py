#Exercicio 1
i = 13 
soma = 0 
k = 0

while k < i:
    k = k + 1

    soma = soma + k

print(soma)

#Exercicio 2:
def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]

def verifica_pertence(numero, fibonacci):
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
fibonacci = fibonacci_sequence(numero)
print(verifica_pertence(numero, fibonacci))

#Exrecicio 5:
nome = input('Digite seu nome ').upper()
valor = f'seu nome invertido é {nome[::-1]}'
print(valor )
