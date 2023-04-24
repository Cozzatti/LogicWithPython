#Lógica de programação

# Seu nome aqui: Gabriel Machado Cozzatti

# Competências a serem avaliadas:

# - Saber interpretar corretamente o que foi pedido;

# - Desenvolver uma solução viável para o problema proposto;

# - Saber utilizar os comandos/funções vistos durante o semestre;

# - Saber utilizar listas.

nome=[]
idade=[]
peso=[]
altura=[]
IMC=[]

def limpatela():
    print('\n' *30)
def menu():
    limpatela()
    print('Escolha uma opção: ')
    print('1 - Incluir Aluno')
    print('2 – Listar todos alunos e seus dados')
    print('3 - Listar os dados de um aluno')
    print('4 – Listar dados dos alunos de uma determinada Idade')
    print('9 - Fim')
    print("Opção: ",end='')

def incluir(): #inlcuir o aluno
  alu=input("Digite o nome do aluno: ") 
  while (alu): #mantendo o loop enquanto um nome for digitado
    try: #try e except para caso algum erro de digitação ocorra o código continue
        i=int(input("Digite a idade do aluno: "))
        ps=float(input("Digite o peso do aluno: "))
        alt=float(input("Digite a altura do aluno: "))
        nome.append(alu) #colocando as informaçoes nas suas respectivas listas através do comando "append"
        idade.append(i)
        peso.append(ps)
        altura.append(alt)
        imcc = ps/(alt*alt)
        IMC.append(imcc)
    except ValueError: 
      print("Erro de digitação")
    alu=input("Digite o nome do aluno: ")

def listartodosalunos():
    for i in range(nome):
        print(nome[i], idade[i], peso[i], altura[i], IMC[i])
    f=input("Pressione enter para continuar")

def listarumaluno():
    y=input("Digite o nome do aluno: ")
    while (y):
        try:
            x=nome.index(y)
            print(nome[x], idade[x], peso[x], altura[x], IMC[x])
        except ValueError: 
            print("Aluno não encontrado")
        y=input("Digite o nome do aluno: ")

def dadosalunoidade():
    try:
        a=int(input("Digite a idade dos alunos: "))
        soma = 0
        qtd = 0
        while(a):
            for i in range(len(idade)):
                if a == idade[i]:
                    print(nome[i], idade[i], peso[i], altura[i], IMC[i])
                    soma = soma + IMC[i]
                    qtd = qtd + 1
            print("Média IMC: ", soma/qtd)
            a=int(input("Digite a idade dos alunos: "))
    except ValueError:
        print("Não válido")
        

op = 0
while op != 9: #looping para manter o menu se repetindo
        menu()
        try:
            op=int(input())
        except:
            print("Digite novamente ", end='')
            x=input("ENTER continua...")
            op=0
        if op == 1:
            incluir()
        elif op == 2:
            listartodosalunos()
        elif op==3:
            listarumaluno()
        elif op==4:
            dadosalunoidade()
        elif op==9:
            break
        else:
            print("Digite uma opção válida! ")
            x=input("Aperte enter para continuar")
print("Programa encerrado")        
