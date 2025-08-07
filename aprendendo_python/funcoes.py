#FUNÇÕES

def ola_mundo():
    return "Olá Mundo!"

print(ola_mundo())

#Função de soma

def soma(numeroUm, numeroDois):
    return (numeroUm+numeroDois)

#Função verifica se é par ou ímpar
def verificaParOuImpar(numero):
    if(numero % 2 == 0):
        return (f"O número {numero} é par")
    else:
        return (f"O número {numero} é ímpar")

entradaUM = int(input("Insira um número: "))
entradaDOIS = int(input("Insira outro número: "))

entradaParOuImpar = int(input("Insira o número que deseja verificar se é par ou ímpar: "))

print(f"A soma dos números resulta: {soma(entradaUM, entradaDOIS)}")

print(verificaParOuImpar(entradaParOuImpar))

#Função fatorial

def fatorial(numero):
    if(numero == 0):
        return 1
    else:
        return (numero * fatorial(numero-1))

entradaFatorial = int(input("Insira o número que deseja saber o fatorial: "))

print(f"O fatorial desse número é: {fatorial(entradaFatorial)}")

def maiorNumeroLista(lista):
    maior = 0


