'''

1.1 - Faça um algoritmo para imprimir a imagem abaixo.

##########
#         #
#         #
#         #
#         #
#         #
#         #
#         #
#         #
##########

1.2 - Altere o algoritmo anterior para que o usuário digite a altura e o comprimento e ainda em qual coluna a figura inicia.
A altura e o comprimento não podem ser menor que 3.
'''
print("Exercicio 1.1")
linha1 = "#"*10
linha2 = "#"+" "*8+"#"

for x in range(10):
    if x == 0 or x == 9:
        print(linha1)
    else:
        print(linha2)
        
print(" ")
print("Exercicio 1.2")
qtLinhas = int(input("Digite a quantidade de linhas: "))

qtColunas = int(input("Digite a quantidade de linhas: "))
        
linha1 = "#"*qtColunas
linha2 = "#"+" "*(qtColunas-2)+"#"

for x in range(qtLinhas):
    if x == 0 or x == (qtLinhas-1):
        print(linha1)
    else:
        print(linha2)
        
