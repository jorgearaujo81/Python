#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
number = float(input('Informe um número:'))

if number < 0:
    print('O número negativo')
elif number > 0:
    print('O número positivo')
else:
    print('O número zero')