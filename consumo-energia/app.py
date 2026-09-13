# Programa para calcular conumo de energia de aparelhos
print("Olá aqui você calcula o consumo de energia de seus aparelhos. Para iniciar me responda:")

print("-----------------------------------")

aparelho = (input("Qual o nome do aparelho ? "))
potencia = float(input("Qual a potência do aparelho em watts(W) ? "))
tempo = float(input("Qual o tempo médio de uso diário em horas ?"))
taxafixa = float(0.75)
"""Calculo para saber o consumo mensal do produto digitado em KWh,
utilizando a fórmula a seguir:  """

consumomensal = (potencia * tempo * 30) / 1000
custoestimado = (consumomensal*taxafixa)

#resultado do cálculo
print("****************************************")
print(f"Nome do aparelho: {aparelho}")
print(f"Consumo estimado: {consumomensal} kWh/mês")
print(f"A estimativa do custo é: R${custoestimado:.2f}")
