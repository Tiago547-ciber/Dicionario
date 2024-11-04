
# Online Python - IDE, Editor, Compiler, Interpreter

dicionario = {
  "Oi": "Oi tudo bem?",
  "Tudo" : "Ótimo. Posso te ajudar com a descrição de qualquer animal. Basta perguntar.",
  "gato" : "O gato (felis catus) é um mamífero carnívoro e quadrúpede pertencente à família Felidae e à ordem carnívora. É um animal doméstico apreciado por caçar ratos e ratazanas. Este animal possui unhas retráteis, ouvidos e olfação bem aguçados, uma notável visão noturna e um corpo flexível, musculoso e compacto.",
  "Gato" : "O gato (felis catus) é um mamífero carnívoro e quadrúpede pertencente à família Felidae e à ordem carnívora. É um animal doméstico apreciado por caçar ratos e ratazanas. Este animal possui unhas retráteis, ouvidos e olfação bem aguçados, uma notável visão noturna e um corpo flexível, musculoso e compacto.",
  "Cachorro" : "O cão da mesma maneira que o lobo, a raposa, etc., possui patas finas e um corpo com um pescoço forte e bem definido que suporta uma cabeça com orelhas grandes e eretas. O focinho é alongado o que está relacionado com um bom sentido do olfato e mandíbulas fortes com dentição carnívora.",
  "cachorro": "O cão da mesma maneira que o lobo, a raposa, etc., possui patas finas e um corpo com um pescoço forte e bem definido que suporta uma cabeça com orelhas grandes e eretas. O focinho é alongado o que está relacionado com um bom sentido do olfato e mandíbulas fortes com dentição carnívora.",
  "O que é um cachorro?": "O cão da mesma maneira que o lobo, a raposa, etc., possui patas finas e um corpo com um pescoço forte e bem definido que suporta uma cabeça com orelhas grandes e eretas. O focinho é alongado o que está relacionado com um bom sentido do olfato e mandíbulas fortes com dentição carnívora.",
  "O que é um gato?" : "O gato (felis catus) é um mamífero carnívoro e quadrúpede pertencente à família Felidae e à ordem carnívora. É um animal doméstico apreciado por caçar ratos e ratazanas. Este animal possui unhas retráteis, ouvidos e olfação bem aguçados, uma notável visão noturna e um corpo flexível, musculoso e compacto.",

}

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

verificar()
