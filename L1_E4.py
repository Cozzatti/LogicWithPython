'''Faça um programa que lê o nome de um produto, a quantidade comprada, 
o valor unitário e o percentual de desconto a ser aplicado para o pagamento. 
Imprima na tela o nome do produto e o valor total da venda.'''
print("Escolha um dos seguintes produtos:\nLEITE\nARROZ\nFEIJÃO\n")
nomeproduto = input("Digite o nome do produto:\n")
quantidade = int(input("Digite a quantidade desejada:\n"))
preço = float(input("Digite o valor do produto:\n"))
desconto = float(input("Digite o tamanho d desconto em porcentagem:\n"))
valordesconto = (quantidade*preço)*(desconto/100)
print("O valor total da compra de ", nomeproduto," é de: ", (quantidade*preço)-valordesconto)


