''' faça um programa que crie duas listas uma com os nomes dos alunos e outra com a média obtida em uma disciplina, use um menu para pedir as seguintes operações
1- incluir na lista
2- listar a lista com nome e média
3- procurar um aluno na lista e mostrar sua média
4- calcula a média da turma
5- fim
'''
#definicao das listas usadas
alunos=[]
medias=[]
#definicao da funcao menu
def menu():
    print("ESCOLHA UMA OPÇÃO:")
    print("1- incluir na lista")
    print("2- listar a lista com nome e média")
    print("3- procurar um aluno na lista e mostrar sua média")
    print("4- calcula a média da turma")
    print("9- fim")
    print("Opção: ",end='')
def incluir():
    print("*" *50)
    nome=input("Digite o nome do aluno: ")
    media=float(input("Digite a media do aluno: "))
    alunos.append(nome)
    medias.append(media)
    print("*" *50)
def listar():
    print("Lista de alunos da disciplina: \n")
    print("*" *50)
    for i in range(len(alunos)):
        print(alunos[i], " Medias  ", medias[i])
def procura():
    print("*" *50)
    print("Lista de alunos da disciplina: \n")
    nome=input("Digite o nome do aluno: ")
    

#inicio do programa
op=0
while op!=9:
#tentativa 
    try:
        menu()
        op=int(input())
        if op==1:
            incluir()
        elif op==2:
            listar()
        elif op==3:
            procura()
#caso ocorra um erro na tentativa:
    except:
        print("Digite novamente")