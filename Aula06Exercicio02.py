# Aula06 - Exercicio 02
# Autor: Eduardo Caetano


'''
Faça um algoritmo que leia um valor equivalente ao saque de um caixa automático,
mostre quantas cédulas são necessárias para pagar o valor solicitado.
Considerar notas de 100, 50, 20, 10 e 5 Reais.

Caso o valor solicitado não seja possível ser pago, mostre a seguinte mensagem:
"Valor não pode ser pago"

Exemplo:
Digite o valor de saque: 270
Para pagar o valor solicitado são necessários:
2 notas de 100 Reais
1 nota de 50 Reais
1 nota de 20 Reais
'''

valor = int(input("Digite o valor: "))

print("Para pagar o valor solicitado são necessários:")


#print("\n",valor//50, " notas de 50 Reais ",end="")
#if valor%50 > 0:
#    print(" e faltam ainda ",valor%50, " Reais")
val1, val2, val3, val4, val5 = 0, 0, 0, 0, 0 
resto1, resto2, resto3, resto4, resto5 = 0, 0, 0, 0, 0 

#------------------------------------------
if valor%50 !=0:
    val1 = (valor//50)
    resto1 = (valor%50)
    print(val1," notas de 50 Reais")
else:
    print(val1," notas de 50 Reais")
    resto1 = 0
#------------------------------------------
if resto1 != 0:
    val2 =(resto1//20)
    resto2=(resto1%20)
    print(val2," notas de 20 Reais")
else:
    print(val2," notas de 20 Reais")
    resto1 = 0
#------------------------------------------
if resto2 != 0:
    val3 =(resto2//10)
    resto3=(resto2%10)
    print(val3," notas de 10 Reais")
else:
    print(val3," notas de 10 Reais")
    resto3 = 0
#------------------------------------------
if resto3 != 0:
    val4 =(resto3//5)
    resto4=(resto3%5)
    print(val4," notas  de 5 Reais")
else:
    print(val4," notas  de 5 Reais")
    resto4 = 0
#------------------------------------------ 
if resto4 != 0:
    val5 =(resto4//1)
    resto5=(resto4%1)
    print(val5," Moedas de 1 Reais")
else:
    print(val5," Moedas de 1 Reais")
    resto5 = 0
#------------------------------------------ 


