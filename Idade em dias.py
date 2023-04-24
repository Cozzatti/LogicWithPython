''' Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, 
meses e dias. '''
diasidade = int(input("Digite sua idade em dias: "))
anosidade = int(diasidade/365)
sobradias = diasidade%365
meses = int(sobradias/30)
dias = int(sobradias%30)

print("A sua idade é", anosidade, "anos", meses, "meses e", dias, "dias")

