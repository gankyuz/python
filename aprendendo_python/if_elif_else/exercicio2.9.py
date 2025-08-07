"""Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
"""
frutas = {"Maçã": 1.50, "Banana": 2.75, "Uva": 1.90,
          "Pera": 1.25,
          "Laranja": 0.65,
          "Limão": 1.25,
          "Goiaba": 2.15,
          "Abacaxi": 3.20,
          "Jaca": 5.80}

fruta_usuario = input("Informe a fruta desejada: ")

"""
for chave,valor in frutas.items():
    if fruta_usuario == chave :
        print(f"{fruta_usuario}: R${valor:.2f}")
"""



if fruta_usuario in frutas:
    print(frutas[fruta_usuario])
else:
    print("Entre com um valor válido!")
