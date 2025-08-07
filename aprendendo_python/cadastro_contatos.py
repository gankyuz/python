"""Cadastro de contatos
Crie um programa que permita cadastrar nome, telefone e e-mail em um dicionário. Depois, permita listar os contatos."""

dados_contatos = {}

while(True):
   nome = input("Digite o nome do contato que deseja salvar: ")
   telefone = int(input("Digite o telefone do contato que deseja salvar: "))
   email = input("Digite o email do contato que deseja salvar: ")

   dados_contatos[nome] = {
       "Telefone": telefone,
       "Email": email
   }

   continuar = input("Deseja continuar(s/n)? ")
   if continuar.lower() == "n":
       for nome, info in dados_contatos.items():
           print(f"Nome: {nome}")
           print(f"Telefone: {info['Telefone']}")
           print(f"Email: {info['Email']}\n")
       break




