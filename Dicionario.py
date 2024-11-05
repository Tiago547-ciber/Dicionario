
# Online Python - IDE, Editor, Compiler, Interpreter

import json
with open("formatted.json", "r") as arquivo:
    dicionario = json.load(arquivo)

def verificar():
  for i in range(5000):
    a = input("Digite uma palavra.")
    if a not in dicionario:
      dicionario[a] = True
      print("Não entendi. Poderia perguntar novamente?")
    elif a in dicionario:
      print(dicionario[a])
    else:
      print("a palavra ja existe.")
    with open("formatted.json", "w") as arquivo:
        json.dump(dicionario, arquivo, indent=4)


verificar()
