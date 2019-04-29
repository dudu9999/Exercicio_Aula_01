'''
# Autor: Eduardo Caetano
Exercicio 1.1 - Faça um algoritmo para imprimir a imagem abaixo.
#
##
###
####
#####
######
#######
########
#########
##########

1.2 - Altere o algoritmo para que o usuário digite a quantidade
linhas que ele desejar.
'''
# exemplo 1

print("Exercicio 1.1")
print(" ")
for x in range(1,11):
    print("#"*x)

# exemplo 2
print("_________________________________")
print(" ")
print("Exercicio 1.2")
print(" ")
qtLinhas = int(input("Digite a quantidade de linhas: "))+1

for x in range(1,qtLinhas):
    print("#"*x)

 
   
    
