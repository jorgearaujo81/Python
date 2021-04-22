#Uma empresa deseja reavaliar os salários dos seus funcionários.
# Será reajustado o salário daqueles que estão há 2 anos ou mais sem receber aumento.
# O ajuste acontecerá da seguinte forma:
# Funcionário com mais de 10 anos de casa, 30%.
# Funcionário que tem entre 5 a 10 anos de casa, 20%.
# Funcionário com menos de 5 anos de casa, 10%.
# Aqueles que receberam aumento salarial há menos de 2 anos não estão aptos ao reajuste salarial coletivo.
# Faça um programa que receba as seguintes informações sobre o funcionário:
# Ano de admissão, salário atual, ano do último reajuste salarial
# O programa deverá mostrar o novo salário do funcionário ou uma mensagem informando que ele não está apto ao reajuste salarial coletivo
# Em seguida o programa deverá perguntar se o usuário deseja informar os dados de um novo funcionário, ou encerrar o programa.
import datetime
time = datetime.datetime.now()
current_year = time.year
answer = 'S'

while answer == 'S':
    admission_year = int(input('Ano de admissão:'))
    wage = float(input('Salário atual:'))
    adjustment_year = int(input('Ano do último reajuste salaria:'))

    company_time = current_year - admission_year 
    adjustment_time = current_year - adjustment_year

    if adjustment_time >= 2:
        if company_time > 10:
            new_wage = wage + wage * 0.3
        elif company_time >= 5 and tempo_empresa <= 10:
            new_wage = wage + wage * 0.2
        else:
            new_wage = wage + wage * 0.1
        print(f'Novo salário:R${new_wage}')
    else:
        print(f'Você não está apto ao reajuste salarial coletivo.')    
    answer = input(f'Deseja informar os dados de um novo funcionário? S - Sim ou N - Não ')
    answer = answer.title()