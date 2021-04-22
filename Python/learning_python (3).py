#Faça um algoritmo que receba vários números positivos até o usuário digitar 1 e finalizar.
# Informe quantos números o usuário digitou.

number = int(input('Digite um número ou  -1 para parar:'))
count = 0

while number != -1:
    number = int(input())

    if number > 0:
        count +=1

print(f'Quantidade de números positivos:{count}')