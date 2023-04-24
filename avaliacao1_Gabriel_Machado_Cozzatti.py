#Faça um programa que 
#recebe em uma lista o código de cada candidato a CIPA
#Criar uma segunda lista para receber os 
#votos dos candidatos, nas mesmas posições de cada candidato e os 
#brancos e nulos no final da Lista.
#Caso o eleitor digite ZERO colocar como voto em Branco.
#Caso o eleitor digite um número que não existe na lista 
#de candidatos colocar como voto NULO.
#Antes de cada entrada de voto, listar os números dos candidatos.
#A entrada dos votos deve encerrar quando for 
#digitado um voto Negativo.
#Calcule o total de votos e o percentual que cada candidato 
#recebeu. Liste os dois vetores e o percentual que cada candidato 
#recebeu em ralação ao total.
codigo = [1,2,3,4]
votos = []
total = 0
co = int(input("Digite (0) para votar em BRANCO \nDigite (1) para votar em Chunda \nDigite (2) para votar em Jair\n"))
while co>=0:
    if co == 1:
        total = total + 1
        v = 'Chunda'
    elif co == 2:
        total = total + 1
        v = 'Jair'
    elif co == 0:
        total = total + 1
        v = 'BRANCO'
    elif co !=0 and co !=1 and co!=2:
        total = total + 1
        v = 'NULO'
    votos.append(v)
    co = int(input("Digite (0) para votar em BRANCO \nDigite (1) para votar em Chunda \nDigite (2) para votar em Jair\n"))
print("TOTAL DE VOTOS: ", total)
cont =  0
for i in range(len(votos)):
    if votos[i] == 'Chunda':
        cont+=1
print("Chunda: ", (cont*100)/total,"%")
cont =  0
for i in range(len(votos)):
    if votos[i] == 'Jair':
        cont+=1
print("Jair: ", (cont*100)/total,"%")
cont =  0
for i in range(len(votos)):
    if votos[i] == 'BRANCO':
        cont+=1
print("BRANCO: ", (cont*100)/total,"%")
cont =  0
for i in range(len(votos)):
    if votos[i] == 'NULO':
        cont+=1
print("NULOS: ", (cont*100)/total,"%")

    
