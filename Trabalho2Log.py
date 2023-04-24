'''
Faça um programa que crie  listas para conter:
a) CÓDIGO: código de um produto
b) NOME: nome do Produto
c) ESTOQUE: estoque do Produto 
d) VENDA: enda do Produto(colocar o codigo do Produto Vendido)
c) QTD: quantidade vendida do Produto 
obs.: Nas listas a,b,c os índices equivalem a um mesmo produto

Use um menu para pedir as seguintes operações:
1 - Incluir Produto
2 - Realizar uma Venda 
3 - Listar todas as vendas  de um produto
4 - Listar todas as vendas
5 - Listar estoque de um Produto
6 - Listar estoque de todos Produtos
9 - fim
Faça para: 
1) Incluir Produto: 
Digite o código, Nome, e estoque e inclua nas respectivas listas CODIGO, NOME, ESTOQUE, usando o mesmo índice por produto,  Digite enquanto o codigo do produto não for VAZIO.
2) Realizar Venda 
Digite o código e a quantidade vendida, inclua nas respectivas listas, VENDA e QTD, após diminuir da tabela estoque conforme o código do Produto digitado. (Procurar na tabela CODIGO o índice respectivo e diminuir da tabela ESTOQUE) 
3)  Listar todas as vendas  de um produto
Pedir um código para listar todas as vendas do produto,CODIGO,NOME,QTD.  verificar se o código existe na lista CODIGO e listar todos os registros da QTD vendida. Encerrar quando digitar um codigo vazio.
4) Listar todas as Vendas
Listar CODIGO, NOME, e QTD vendida de todos Produtos
5) Listar ESTOQUE de um produto
 Pedir um código, verificar se o código existe na lista, para listar o CODIGO, NOME e ESTOQUE do produto.   Encerrar quando digitar um codigo vazio.
6)  Listar  os ESTOQUES  de todos produtos
Listar o CODIGO, NOME e ESTOQUE de todos produtos.
9) FIM 
Encerra Programa 
'''
from statistics import quantiles

codpro = [] #lista para os códigos dos produtos
nome = [] #nome dos produtos
estoque = [] #estoque de cada produto
venda= [] #lista para controlar cada venda (colocando o código de cada produto)
quantidade = [] #quantidade vendida em cada venda (subtrai do estoque)

def limpatela(): #limpar a tela (printa 30 vezes um pular linha "\n")
  print('\n' *30)
def menu(): #menu basico para organizar as opçoes, facilitando pro usuario
  limpatela()
  print('1 - Incluir produto')
  print('2 - Realizar venda')
  print('3 - Listar vendas de um produto')
  print('4 - Listar todas as vendas')
  print('5 - Listar ESTOQUE de um produto')
  print('6 - Listar os ESTOQUES de todos os produtos')
  print('9 - ENCERRAR PROGRAMA')
  print("Opção: ",end='')
def incluir(): #inlcuir o produto no estoque, pedindo para o usuário o código, nome e quantia que será colocada em estoque
  cod=input("Digite o código do produto: ") 
  while (cod): #mantendo o loop enquanto um codigo for digitado
    try: #try e except para caso algum erro de digitação ocorra o código continue
        n=input("Digite o nome do produto: ")
        est=int(input("Digite a quantidade do produto em estoque: "))
        codpro.append(cod) #colocando as informaçoes nas suas respectivas listas através do comando "append"
        nome.append(n)
        estoque.append(est)
    except ValueError: 
      print("Erro de digitação")
    cod=input("Digite o código do produto: ")
x=0
q=0
def realizavenda(): #realizar alguma venda
    y=input('Digite o código do produto a ser vendido: ') #digitar o códito do produto a ser vendido
    while (y): #enquanto houver um código digitado (variavel y) o loop continua
        try:
            x=codpro.index(y) #variável x confere se o código digitado está presente na lista de produtos incluidos (codpro)
            q=int(input('Digite a quantidade a ser vendida: '))
            if estoque[x]<q: #confere se o estoque do item digitado é menor do que a quantia que queremos vender
                print("Número restante no estoque será menor que ZERO. Não é possível realizar venda. Quantidade disponível em estoque: ", estoque[x])
            else: #se a quantia em estoque for maior ou igual a que queremos vender, então realiza as açoes de adicionar as informaçoes nas listas e subtrair a quantia vendida pelo respectivo numero em estoque
                venda.append(y)
                quantidade.append(q)
                estoque[x]=estoque[x]-q
                print("Código do produto: ",codpro[x],"\nQuantidade restante em estoque: ", estoque[x],"\nVendas: ", venda[x], quantidade[x])
        except ValueError: #se o produto nao esta cadastrado ou se foi digitado errado:
            print("O produto não está cadastrado no sistema | NÃO FOI ENCONTRADO")
        y=input('Digite o código do produto a ser vendido: ')
      
def listavendaprod():  #listar a venda de um produto especifico
    y=input("Digite o código do produto: ")
    while(y): #mantendo o loop enquanto algo for digitado na variavel y (codigo do produto)
        try:
            x=venda.index(y) #procura o codigo na lista de vendas
            z=codpro.index(y) #procura o codigo na lista de codigos incluidos
            print("Vendas desse produto: ", venda[x], nome[z], quantidade[x],"\n")
        except ValueError: #caso o produto nao tenha sido cadastrado ou nao tenha sido vendido ainda:
            print("Produto não cadastrado | Nenhuma venda")
        y=input("Digite o código do produto: ")
def listatodasvendas(): #lista todas as vendas de todos os produtos
    for i, e in enumerate(venda): #varre a ordem da lista de vendas 
        y=codpro.index(e) #alinha a coluna da lista de codigos incluidos com a lista de vendas caso 
        print(venda[i], nome[y], quantidade[i]) 
    f=input("Pressione enter para continuar") 
def verestoqueprod(): #ver estoque de um produto específico
    y=input("Digite o código do produto: ")
    while(y): #mantém o loop enquanto um códito (varivel y) é digitado
        try:
            x=codpro.index(y) #confere se o código digitado existe na lista de produtos incluídos
            print("Estoque: ", venda[x], nome[x], estoque[x])
        except ValueError: 
            print("Produto não cadastrado/Não encontrado")
        y=input("Digite o código do produto: ")


def listartodosestoques(): #listar todos estoques
    for i in range(len(codpro)):
        print(codpro[i], nome[i], estoque[i]) #pelo fato dessas listas já estarem "alinhadas", só é necessário imprimí-las dentro de um for que as varre
    m=input("Digite enter para continuar")
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
            realizavenda()
        elif op==3:
            listavendaprod()
        elif op==4:
            listatodasvendas()
        elif op==5:
            verestoqueprod()
        elif op==6:
            listartodosestoques()
        elif op ==9:
            break
        else:
            print("Criatura só uma das opções válidas!")
            x=input("ENTER continua...")
print("FIM")