

import json
with open("pedidos.json", "r") as arquivo:
    dicionario = json.load(arquivo)

def verificar():
  for i in range(5000):
    print("Olá. Digite o número do seu pedido de compra, para saber o status de entrega.")
    a = input()
    if a not in dicionario:
      print("O número do pedido esta incorreto ou não existe.")
    elif a in dicionario:
      print(dicionario[a][2])

    else:
      print("Erro.")
    with open("formatted.json", "w") as arquivo:
        json.dump(dicionario, arquivo, indent=4)


verificar()
