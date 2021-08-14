def teste(arquivo):
    try:
        a = open(arquivo, "rt")
        a.close()
    except FileNotFoundError:
        a = open(arquivo, "wt+")
        print("Arquivo Criado")
    else:
        print("Arquivo Já existente")


def escrever(arquivo, livro, autor):
    try:
        a = open(arquivo, "at+")
    except:
        print("Erro Ao adicionar dados!!!")
    else:
        try:
            a.write(f" -{livro} - {autor}\n")
        except:
            print("Erro Ao adicionar dados!!!")
        else:
            print("Dados Adicionados com sucesso!!")

