#O codigo com o menu

#o código lendo vários alunos é a mesma coisa
#a única diferença é que ele está dentro de uma repetição
#de um enquanto
escolha = int(input("Menu: 1 Cadastro  -  2 Relatório"))
nome = ""
faltas = 0
nota1, nota2, nota3, nota4, media = 0.0
situacao = ""
#Com o menu a diferença é que agora o código de cadastro depende de um SE
#de uma escolha do usuário, ou seja, o código só será executado se o usuário escolher
if escolha == 1:
    situacao = ""
    quantidade_alunos = float(input("Deseja calcular a média de quantos alunos"))

    cont = 0
    while cont < quantidade_alunos:
        nome = input("Digite o nome do aluno ")
        faltas = float(input("Digite as faltas do aluno "))
        #4 NOTAS
        nota1 = float(input("Digite a 1 nota do aluno "))
        nota2 = float(input("Digite a 2 nota do aluno ")) 
        nota3 = float(input("Digite a 3 nota do aluno "))
        nota4 = float(input("Digite a 4 nota do aluno "))


        #calculo média
        media = (nota1+nota2+nota3+nota4)/4 #media final do aluno já está aqui

        #Lógica aprovado / lógica reprovado / recuperação
        if faltas > 30:
            situacao = "Reprovado por Faltas" #Só quero guardar a informação se o aluno passou ou não
        elif media >= 8:
            situacao =  "Aprovado"
        elif media >= 5:
            recuperacao = float(input("Aluno de recuperação. Digite a nota da recuperação:"))
            if recuperacao > (10-media):
                situacao =  "Aprovado na Recuperação"
            else:
                situacao =  "Reprovado na Recuperação"
        else:
            situacao = "Reprovado"
elif escolha == 2:
    #relatorio
    print("Nome: ", nome)
    print("Faltas: ", faltas)
    print(f"Notas: , {nota1} {nota2} {nota3} {nota4}")
    print("Media: ", media)
    print("Situação: ", situacao)
else:
   print("Encerra o programa")