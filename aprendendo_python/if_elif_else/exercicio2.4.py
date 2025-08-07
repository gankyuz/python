from enum import nonmember

import none

notaUM = float(input("Digite a primeira nota: "))
notaDOIS = float(input("Digite a segunda nota: "))
notaTRES = float(input("Digite a terceira nota: "))
notaQUATRO = float(input("Digite a quarta nota: "))

notas = [notaUM, notaDOIS, notaTRES, notaQUATRO]

media = sum(notas)/len(notas)

maiorNOTA = notaUM
menorNOTA = notaUM

if(notaDOIS > maiorNOTA):
    maiorNOTA = notaDOIS
if(notaTRES > maiorNOTA):
    maiorNOTA = notaTRES
if(notaQUATRO > maiorNOTA):
    maiorNOTA = notaQUATRO

if(notaDOIS < menorNOTA):
    menorNOTA = notaDOIS
if(notaTRES < menorNOTA):
    menorNOTA = notaTRES
if(notaQUATRO < menorNOTA):
    menorNOTA = notaQUATRO


print(media, maiorNOTA, menorNOTA)

