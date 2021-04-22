#Faça um algoritmo que receba o ano de nascimento do usuário, o ano atual, e imprima a idade.
year_birth = int(input('Ano de nascimento:'))
current_year = int(input('Ano atual:'))
age = current_year - year_birth

print(f'idade:{age}')