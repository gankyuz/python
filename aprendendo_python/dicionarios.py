# Dicionários são pares de chaves/valor

dados_gabi = {"nome":"Gabi",
              "mãe":"Fabiana",
              "pai":"Valquires",
              "solteira":True,
              "escolaridade":["Ensino Médio","Graduanda em Ciência da Computação"],
}

# <codecell>
print(dados_gabi["solteira"])
# <codecell>
dados_gabi["idade"] = 20
print(dados_gabi)
# <codecell>
print(dados_gabi.keys())
print(dados_gabi.values())
print("Items:", dados_gabi.items())
# <codecell>
for i in dados_gabi:
    print(i, "->", dados_gabi[i])
# <codecell>

for [chave,valor] in dados_gabi.items():
    print(chave, "->", valor)

