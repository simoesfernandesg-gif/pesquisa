# importa a biblioteca para deixar a tela limpa, utilizando cls para Windows e clear para Linux ou Mac
import os
os.system ("cls" if os.name =="nt" else "clear")

# Mostra o título centralizado
print("Classificação de perfil".center(50))

# Entrada de dados: tipo de imóvel e pede ao usuário o consumo mensa de água em metro cúbico (m3)
opcao = input (" Digite o tipo de imóvel (comercial, casa ou apartamento): ").lower()
consumo = float (input("Digite o consumo mensal de água (m3): "))

""" Processamento de dados: o usuário digita uma das opções acima e o consumo mensal de aguá, 
aqui aparecerá a msg para cad tipo de imóvel."""

match opcao: 
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    case "apartamento" if consumo <10:
        print ("Consumo econômico – excelente controle de água!") 
        
    case "apartamento" | "casa" if  consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")    

    case _:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")       
