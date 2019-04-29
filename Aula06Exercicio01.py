# Aula06 - Exercicio 01
# Autor: Eduardo Caetano
'''
Faça um algoritmo que leia um valor em dinheiro e mostre, para esse valor,
quantas notas de:
50,00 Reais são necessárias para pagar esse valor e, quanto faltaria pagar.
20,00 Reais são necessárias para pagar esse valor e, quanto faltaria pagar.
10,00 Reais são necessárias para pagar esse valor e, quanto faltaria pagar.

Exemplo:
Digite um valor em dinheiro:  340
Para esse valor são necessárias:
6 notas de 50 Reais e faltam ainda 40 Reais
17 notas de 20 Reais
34 notas de 10 Reais
'''



valor = int(input("Digite o valor: "))


print("Para pagar o valor solicitado são necessários:")

print("\n",valor//50, " notas de 50 Reais ",end="")
if valor%50 > 0:
    print(" e faltam ainda ",valor%50, " Reais")

print("\n",valor//20, " notas de 20 Reais ",end="")
if valor%20 > 0:
    print(" e faltam ainda ",valor%20, " Reais")
print()

print("\n",valor//10, " notas de 10 Reais ",end="")
if valor%10 > 0:
    print(" e faltam ainda ",valor%10, " Reais")



'''
valor = int(input("Digite o valor: "))


print("Para pagar o valor solicitado são necessários:")


if valor%50 > 0:
    faltaAinda = " e faltam ainda "+str(valor%50)+ " Reais"
else:
    faltaAinda = ""
print(valor//50, " notas de 50 Reais "+faltaAinda)


if valor%20 > 0:
    faltaAinda = " e faltam ainda "+str(valor%20)+ " Reais"
else:
    faltaAinda = ""
print(valor//20, " notas de 20 Reais "+faltaAinda)


if valor%10 > 0:
    faltaAinda = " e faltam ainda "+str(valor%10)+ " Reais"
else:
    faltaAinda = ""
print(valor//10, " notas de 10 Reais "+faltaAinda)

'''




