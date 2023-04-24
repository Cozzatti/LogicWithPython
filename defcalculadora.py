def calculadora(a,oper, b):
    if oper=='+':
        c = a+b
    elif oper=="-":
        c = a-b
    return c
def menu():
    print('Digite um número, uma operação e outro número: ')
    print('Operações:\n(+)\n(-)\n(*)\n(/)\n(%)')
for i in range(5):
    menu()
    x=int(input("Digite o valor inteiro"))
    op=input("Digite a operação")