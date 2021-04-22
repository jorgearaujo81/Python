#Faça um programa que receba notas de alunos, até 1 ser informado.
# Ao final da execução, o programa deve exibir quantas notas foram informadas e a média entre elas.
nota = float(input('Digite a nota ou -1 para sair:'))
count = 0
sum = 0

while nota != -1:
    count +=1
    sum += nota
    nota = float(input('Digite a nota ou -1 para sair:'))

average = float(sum / count)
print(f'Foram informadas {count}')
print(f'A média do aluno é {average}')