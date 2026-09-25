#Importa a biblioteca do Windows e limpa a tela com o cls se for mac ou linux, utiliza o clear
import os
os.system ("cls" if os.name == "nt" else "clear")

soma = 0.0
cont_excelente = 0
cont_ruim = 0

#entrada de dados: nome, idade e opnião, dentro da estrutura FOR para limitar a pesquisa em 50.
for i in range(1,51):   
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int (input(" DIgite 1-EXCELENTE, 2-BOM e 3-RUIM: "))

# Estruturas de decisão para contar as opiniões excelente e ruim.
    if opiniao == 1:
        cont_excelente += 1
    elif opiniao == 3:
        cont_ruim += 1   

#exibindo a quantidade de cada opnião        
print(f"Quantidade de opnião EXCELENTE é = {cont_excelente} ")
print(f"Quantidade de opnião RUIM é = {cont_ruim}")   
print ("****Obrigado por participar da pesquisa!****".center (50))
