import time
from time import sleep

entrada = int(input(""))

while (entrada >= 0):
    print(entrada)
    entrada -= 1
    time.sleep(1)

print("Contagem regressiva finalizada!")


