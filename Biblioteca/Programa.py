from Biblioteca.imports import atualizarDB, escritas, leituras, procura
from time import sleep
from Biblioteca.imports.Backup import *
arq = "Backup.txt"
teste(arq)
print("\033[1;97m--" * 100)
print(f"{'Cadastrador de Livros':^45}")
while True:
    escritas.inicio()
    num = leituras.intput("Sua Opção: ")
    print("--" * 100)
    while num > 10 or num < 0:
        print("\033[1;31mValor Inválido\033[m")
        print("--" * 100)
        num = leituras.intput("Sua Opção: ")
        print("--" * 100)
    if num == 1:
        escritas.mostrarautor()
    elif num == 2:
        escritas.mostrarlivros()
    elif num == 4:
        leituras.lerlivro()
    elif num == 3:
        leituras.lerautor()
    elif num == 5:
        escritas.escreverautorelivro()
    elif num == 6:
        procura.procurarlivro()
    elif num == 7:
        atualizarDB.alterar()
    elif num == 8:
        procura.procurarescritor()
    elif num == 9:
        break
    sleep(0.5)
escritas.fim()
