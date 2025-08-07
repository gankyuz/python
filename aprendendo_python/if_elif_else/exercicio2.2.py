"""Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

	O número x é impar
ou
	O número x é par
"""

def imparOUpar(numero):
    if(numero % 2 == 0):
        return(f"O número {numero} é par")
    else:
        return (f"O número {numero} é ímpar")

numero = int(input("Digite um número(inteiro): "))

print(imparOUpar(numero))