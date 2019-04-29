# Autor: Eduardo Caetano
'''
Faça um algoritmo para imprimir a imagem abaixo.
                    #
                   ###
                  #####
                 #######
                #########
               ###########
              #############
             ###############
            #################
           ################### 

Altere o algoritmo para que o usuário digite a coluna inicial
(ponta) e a quantidade de linhas.
'''
c = "#"
d = 20
e = 2
print("                     #")
for x in range(0, 9):
	print((d*" ")+"#"+(e*c))
	d = d -1
	e = e +2
