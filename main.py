numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
soma = 0

for numero in range (numero_1 , numero_2):
    if numero % 2 == 0:
        soma += numero
        print(soma)
    elif numero % 2 == 1:
        print('não há numeros pares nesse intervalo')             