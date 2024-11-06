
with open("formatted.json", "r") as arquivo:
    dicionario = json.load(arquivo)

def cadastro():
    nome = input("Digite o  nome")
    cpf = input("Digite o cpf")
    pedido = input("Digite o numero do pedido")

    if nome and cpf and pedido not in dicionario:
       dicionario[pedido] = nome, cpf, True
       print("Pedido cadastrado com sucesso")
       with open("formatted.json", "w") as arquivo:
            json.dump(dicionario, arquivo, indent=4)


cadastro()