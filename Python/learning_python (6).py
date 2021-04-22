#Faça um Programa que peça dois números e imprima o maior deles.
number1 = float(input('Informe o primeiro número:'))
number2 = float(input('Informe o segundo número:'))

if number1 > number2:
    print(f'O maior número é {number1}')
else:
    print(f'O maior número é {number2}')