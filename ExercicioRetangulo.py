# Aula05 Exercício 01 - Figuras
# Eduardo Caetano

'''
1.1 - Faça um algoritmo para imprimir a imagem abaixo. (10 x 10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

1.2 - Altere o algoritmo anterior para o usuário digitar em qual
coluna ele quer começar a montar a figura.

coluna 4
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

'''

print("Exercicio 1.1 ")
print(" ")
linha = "#"*10
for x in range(10):
    print(linha)

#------------------------------------
print(" ")
print("Exercicio 1.2")
print(" ")

valor = int(input("Digite a coluna para iniciar a figura: "))

linha = "#"*10
for x in range(10):
    print(linha.rjust(len(linha)+valor))







