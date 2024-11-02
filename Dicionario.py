
# Online Python - IDE, Editor, Compiler, Interpreter

dicionario = {}

def verificar():
  for i in range(5000):
    a = input("Digite uma palavra.")
    if a not in dicionario:
      dicionario[a] = True
      print(dicionario)
    else:
      print("a palavra ja existe.")

verificar()
