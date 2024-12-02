#com FUNÇÕES cada parte do código fica isolada das outras, melhorando a legibilidade do codigo
#e facilitando a manutenção

#-----------------------------------------------------Função para calcular a média e situação do aluno
def calcular_media_e_situacao(faltas, notas):
    media = sum(notas) / len(notas)  # Média das 4 notas
    situacao = ""
    if faltas > 30:
        situacao = "Reprovado por Faltas"
    elif media >= 8:
        situacao = "Aprovado"
    elif media >= 5:
        recuperacao = float(input("Aluno de recuperação. Digite a nota da recuperação: "))
        if recuperacao > (10 - media):
            situacao = "Aprovado na Recuperação"
        else:
            situacao = "Reprovado na Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao


#-----------------------------------------------------Função para gerar o relatório
def gerar_relatorio(alunos):
    if alunos:
        for aluno in alunos:
            print(f"Nome: {aluno[0]}")
            print(f"Faltas: {aluno[1]}")
            print(f"Notas: {', '.join(map(str, aluno[2]))}")
            print(f"Média: {aluno[3]}")
            print(f"Situação: {aluno[4]}")
            print("-" * 30)
    else:
        print("Nenhum aluno cadastrado ainda.")


#-----------------------------------------------------Função para cadastrar um aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    faltas = float(input("Digite as faltas do aluno: "))
    notas = []
    for i in range(4):
        notas.append(float(input(f"Digite a {i + 1}ª nota do aluno: ")))
    media, situacao = calcular_media_e_situacao(faltas, notas)
    # Retorna os dados do aluno
    return [nome, faltas, notas, media, situacao]


# -----------------------------------------------------Função principal
def menu_principal():
    alunos = []  # Lista que armazenará todos os alunos cadastrados
    while True:
        print("\nMenu:\n 1 - Cadastro de Aluno // 2 - Relatório de Alunos // 3 - Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))
            for _ in range(quantidade_alunos):
                aluno = cadastrar_aluno()
                alunos.append(aluno)
        elif escolha == 2:
            gerar_relatorio(alunos)
        elif escolha == 3:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


            
# Chama a função principal para rodar o menu
menu_principal()
    