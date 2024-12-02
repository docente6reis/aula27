#para possibilitar que após cadastrarmos alunos esses dados fiquem accessiveis para "sempre"
#Precisamos dar um jeito de usar uma estrutura que guarda mais de uma informaç~çao ao mesmo tempo

#O codigo com o menu

#o código lendo vários alunos é a mesma coisa
#a única diferença é que ele está dentro de uma repetição
#de um enquanto
alunos = [] #Array que guardará todos os alunos cadastrados
nome = ""
faltas = 0
notas = []
nota1 = nota2 = nota3 = nota4 = media = 0.0
situacao = ""
#Com o menu a diferença é que agora o código de cadastro depende de um SE
#de uma escolha do usuário, ou seja, o código só será executado se o usuário escolher
while True:
    escolha = int(input("Menu: 1 Cadastro  -  2 Relatório \n"))
    if escolha == 1:
        situacao = ""
        quantidade_alunos = float(input("Deseja calcular a média de quantos alunos\n"))

        cont = 0
        while cont < quantidade_alunos:
            nome = input("Digite o nome do aluno ")
            faltas = float(input("Digite as faltas do aluno "))
            #4 NOTAS
            for i in range(4):
                notas.append(float(input(f"Digite a {i + 1} nota do aluno ")))
                


            #calculo média
            media = (notas[0]+notas[1]+notas[2]+notas[3])/4 #media final do aluno já está aqui

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

            alunos.append([nome, faltas, notas, media, situacao])
            cont += 1

    elif escolha == 2:
        #relatorio
       
       for aluno in alunos:
           print(f"Nome {aluno[0]}\n Faltas: {aluno[1]} \n Notas: {', '.join(map(str, aluno[2]))} \n Media: {aluno[3]} \n Situação: {aluno[4]}")