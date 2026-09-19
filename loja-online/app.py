#Importa a biblioteca do Windows e limpa a tela com o cls se for mac ou linux, utiliza o clear
import os
os.system ("cls" if os.name == "nt" else "clear")

"""programa para calcular descontos em compras online 
   Compras acima de R$ 300 desconto de 15%, maior ou igual a R$ 200 desconto de 10%, 
   menor que R$ 200 deconto de 5%
"""

valor_compra = float (input ("Olá, digite o valor total da sua compra: R$ "))

# Se o valor menor que zero aparecerá a mensagem
if valor_compra <= 0:
     print ("Digite um valor maior que 0.")

# valor maior ou igual a 300 desconto de 15%, utilizando o cálculo desconto = (valor_compra*15)/100
elif valor_compra >= 300:
    desconto = (valor_compra*15)/100
    valor_final = valor_compra - desconto
    print (f" Você teve desconto de 15%. Valor total da sua compra: R$ {valor_final:.2f}")
    print ("*** Obrigado por comprar com a gente! ***".center(60))

# valor maior ou igual a 200 desconto de 10%, utilizando o cálculo desconto = (valor_compra*10)/100
elif valor_compra >= 200:
    desconto = (valor_compra*10)/100
    valor_final = valor_compra - desconto
    print (f" Você teve desconto de 10%. Valor total da sua compra: R$ {valor_final:.2f}")
    print ("*** Obrigado por comprar com a gente! ***".center(60))
# Se não for nenhum dos valores acima, ou seja menor que 200 desconto de 5%, desconto = (valor_compra*5)/100 """
else:
    desconto = (valor_compra*5)/100
    valor_final = valor_compra - desconto
    print (f" Você teve desconto de 5%. Valor total da sua compra: R$ {valor_final:.2f}")
#Centralizando a mensagem a seguir
    print ("*** Obrigado por comprar com a gente! ***".center(60))