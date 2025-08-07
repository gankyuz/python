sair = "nao"
cont = 0
while(sair == "nao"):
    cont = 1
    numero = int(input("Digite um número que deseja saber a tabuada: "))
    while(cont <= 10):
        print(f"{numero} X {numero} = {numero*cont}")
        cont+=1
    sair = input("Deseja sair(SIM ou NAO): ").islower()



