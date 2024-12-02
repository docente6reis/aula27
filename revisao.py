#LER ENTRADAS DO USUÁRIO
nome = input()#ARMAZENAR o nome do aluno
nota1 = float(input())# 4 notas do aluno
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

faltas = int(input())
#calculo da média
media = (nota1+nota2+nota3+nota4)/4

#LOGICA DA SITUAÇÃO
if faltas > 31:
    situacao = "Reprovado por falta"
elif media >= 8:
    situacao = "Aprovado"
elif media >= 5: #recuperação
    recuperacao = float(input())#ler a nota da prova de recuperação
    if recuperacao >= (10-media):
        situacao = "Aprovado na recuperação"
    else:
        situacao = "rEPROVADO NA RECUPERAÇÃO"
else:
    situacao = "Reprovado por média"

#RELATORIO
print("Nome: ", nome)
print("Notas: ", nota1, nota2, nota3, nota4)
print("Faltas:", faltas )
print("Media: ", media)
print("Situacao: ", situacao)