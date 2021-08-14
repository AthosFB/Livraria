import mysql.connector
from Biblioteca.imports import leituras
from time import sleep
from sys import stdout
from Biblioteca.imports.Backup import *
arq = "Backup.txt"
teste(arq)
cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
mcursor = cnx.cursor()
mcursor.execute("use biblioteca")
print("\033[1;97m--" * 100)
print(f"{'Cadastrador de Livros':^45}")
while True:
    print("--" * 100)
    print(""" O que deseja fazer: 
     [1]- Ver Autores Cadastrados
     [2]- Ver Livros Cadastrados
     [3]- Cadastrar Novo Autor
     [4]- Cadastrar Novo Livro
     [5]- Ver Livros e seus Autores
     [6]- Procurar por Livro Especifico
     [7]- Alterar Alguma Informa��o
     [8]- Procurar Livros de Algum Autor
     [9]- Sair Do Programa""")
    print("--" * 100)
    num = leituras.intput("Sua Op��o: ")
    print("--" * 100)
    while num > 10 or num < 0:
        print("\033[1;31mValor Inv�lido\033[m")
        print("--" * 100)
        num = leituras.intput("Sua Op��o: ")
        print("--" * 100)
    if num == 1:
        mcursor.execute("select * from autores order by idautor;")
        rows = mcursor.fetchall()
        print(f"{'ID':<5}{'NOME':<90}{'NASCIONALIDADE':>10}")
        print("--" * 100)
        for row in rows:
            for enu, i in enumerate(row):
                if enu == 0:
                    print(f"{i:<5}", end="")
                elif enu == 1:
                    print(f"{i:<90}", end="")
                else:
                    print(f"{i:>10}")
    elif num == 2:
        mcursor.execute("select * from livros order by idlivro;")
        rows = mcursor.fetchall()
        print(f"{'ID':<5}{'NOME':<80}{'ID AUTOR':>5}")
        print("--" * 100)
        for row in rows:
            for enu, i in enumerate(row):
                if enu == 0:
                    print(f"{i:<5}", end="")
                elif enu == 1:
                    print(f"{i:<104}", end="")
                else:
                    print(f"{i:>5}")
    elif num == 4:
        nomelivro = str(input("Nome do Livro: ")).title().strip()
        print("--" * 100)
        mcursor.execute("select * from autores order by idautor;")
        rows = mcursor.fetchall()
        print("--" * 100)
        print(f"{'ID':<5}{'NOME':<90}")
        print("--" * 100)
        for row in rows:
            for enu, i in enumerate(row):
                if enu == 0:
                    print(f"{i:<5}", end="")
                elif enu == 1:
                    print(f"{i:<90}")
        print("--" * 100)
        print("Se o autor n�o estiver cadastrado (7777)")
        print("--" * 100)
        idautor = int(input("id do Autor: "))
        print("--" * 100)
        if idautor == 7777:
            print("\033[1;32mNada Adicionado\033[1;97m")
        else:
            print("\033[1;32mLivro Cadastrado Com Sucesso!\033[1;97m")
            mcursor.execute(f"""select nomeautor from autores
                                       where idautor = {idautor}""")
            rows = mcursor.fetchall()
            for row in rows:
                for i in row:
                    nomedoautorBackup = i
            print("--" * 100)
            escrever(arq, nomelivro, nomedoautorBackup)
            mcursor.execute(f"insert into livros value (default, '{nomelivro}', '{idautor}')")
    elif num == 3:
        nomeautor = str(input("Nome do autor: ")).title().strip()
        print("--" * 100)
        nascionalidade = str(input("Pa�s de nascionalidade do autor: ")).title().strip()
        print("\033[1;32mAutor Cadastrado Com Sucesso!\033[1;97m")
        mcursor.execute(f"insert into autores value (default, '{nomeautor}', '{nascionalidade}')")
    elif num == 5:
        mcursor.execute("""select l.nomelivro, a.nomeautor from autores as a 
        join livros as l on l.idautor = a.idautor 
        order by a.nomeautor, l.nomelivro;""")
        rows = mcursor.fetchall()
        print(f"{'Livro':<90}{'Autor':>50}")
        print("--" * 100)
        for row in rows:
            for enu, i in enumerate(row):
                if enu == 0:
                    print(f"{i:<100}", end="")
                elif enu == 1:
                    print(f"{i:>50}")
    elif num == 6:
        livro = str(input("Nome do livro: ")).title().strip()
        mcursor.execute(f"""select l.idlivro, l.nomelivro, a.nomeautor, a.nascionalidade
        from livros as l join autores as a 
        on l.idautor = a.idautor
        where nomelivro = '{livro}';""")
        rows = mcursor.fetchall()
        if len(rows) == 0:
            print("--" * 100)
            print("\033[1;31mLivro N�o Cadastrado!\033[1;97m")
        else:
            print("--" * 100)
            print(f"{'ID Livro':<5} | {'Nome Livro':<10} | {'Nome Autor':<10} | {'Nascionalidade':>10}")
            print("--" * 100)
            for row in rows:
                for enu, i in enumerate(row):
                    if enu == 1:
                        print(f"{i}", end=" | ")
                    else:
                        print(f"{i}", end="  |  ")
                print()
    elif num == 7:
        print("""Alterar Informa��o:
[1]- Autores
[2]- Livros""")
        while True:
            print("--" * 100)
            table = int(input("Escolha: "))
            print("--" * 100)
            if table == 1:
                validador = "idautor"
                table = "autores"
                print("""Alterar Informa��o:
[1]- Nome
[2]- Nascionalidade""")
                while True:
                    print("--" * 100)
                    item = int(input("Escolha: "))
                    print("--" * 100)
                    if item == 1:
                        item = "nomeautor"
                        break
                    elif item == 2:
                        item = "nascionalidade"
                        break
                    else:
                        print("\033[1;31mValor inv�lido!\033[1;97m")
                        print("--" * 100)
                break
            elif table == 2:
                validador = "idlivro"
                table = "livros"
                print("""Alterar Informa��o:
[1]- Nome
[2]- Id Autor""")
                while True:
                    print("--" * 100)
                    item = int(input("Escolha: "))
                    print("--" * 100)
                    if item == 1:
                        item = "nomelivro"
                        break
                    elif item == 2:
                        item = "idautor"
                        break
                    else:
                        print("\033[1;31mValor inv�lido!\033[1;97m")
                        print("--" * 100)
                break
            else:
                print("\033[1;31mValor inv�lido!\033[1;97m")
                print("--" * 100)
        if item == "idautor":
            novo = leituras.intput("Coloque o novo Id Autor: ")
            print("--" * 100)
        else:
            mcursor.execute(f"select * from {table};")
            rows = mcursor.fetchall()
            if table == "autores":
                print(f"{'Nome:             Nascionalidade: '}")
                print("--" * 100)
                for row in rows:
                    for enu, i in enumerate(row):
                        if enu == 1:
                            print(f"{i:<30}", end="")
                        elif enu == 2:
                            print(f"{i:>10}")
            else:
                print(f"{'Nome:            Autor:'}")
                print("--" * 100)
                for row in rows:
                    for enu, i in enumerate(row):
                        if enu == 1:
                            print(f"{i:<30}", end="")
                        elif enu == 2:
                            print(f"{i:>5}", end="")
                    print()
            print("--" * 100)
            novo = str(input("Coloque a altera��o: ")).strip().title()
            print("--" * 100)
        escolhido = int(input("Coloque o id  do livro/autor que deseja alterar (9999 n�o sabe o id): "))
        print("--" * 100)
        if escolhido == 9999:
            mcursor.execute(f"select * from {table};")
            rows = mcursor.fetchall()
            print("--" * 100)
            if table == "autores":
                print(f"{'ID':<5}{'NOME':<30}{'NASCIONALIDADE':>10}")
                print("--" * 100)
                for row in rows:
                    for enu, i in enumerate(row):
                        if enu == 0:
                            print(f"{i:<5}", end="")
                        elif enu == 1:
                            print(f"{i:<30}", end="")
                        else:
                            print(f"{i:>10}")
            else:
                print(f"{'ID':<5}{'NOME':<30}")
                print("--" * 100)
                for row in rows:
                    for enu, i in enumerate(row):
                        if enu == 0:
                            print(f"{i:<5}", end="")
                        elif enu == 1:
                            print(f"{i:<30}", end="")
                    print()
        print("--" * 100)
        escolhido = int(input("Coloque o id  do livro/autor que deseja alterar (7777 para cancelar): "))
        print("--" * 100)
        if escolhido == 7777:
            print("\033[1;32mNada alterado\033[1;97m")
            print("--" * 100)
        else:
            mcursor.execute(f"update {table} set {item} = '{novo}' where {validador} = '{escolhido}'")
            print("\033[1;32mAlterado Com Sucesso!\033[1;97m")
    elif num == 8:
        mcursor.execute("select idautor, nomeautor from autores order by nomeautor;")
        rows = mcursor.fetchall()
        print(f"{'ID':<5}{'NOME':<30}")
        print("--" * 100)
        for row in rows:
            for enu, i in enumerate(row):
                if enu == 0:
                    print(f"{i:<5}", end="")
                elif enu == 1:
                    print(f"{i:<30}")
        print("--" * 100)
        selecionado = leituras.intput("Coloque o id do autor desejado: ")
        mcursor.execute(f"""select nomeautor from autores
                            where idautor = '{selecionado}';""")
        rows = mcursor.fetchall()
        print("--" * 100)
        print("Autor:")
        for row in rows:
            for i in row:
                print(f"     -{i}", end=" ")
            print()
        print("--" * 100)
        print("Livros:")
        mcursor.execute(f"""select nomelivro from livros
                         where idautor = '{selecionado}'
                         order by nomelivro""")
        rows = mcursor.fetchall()
        for row in rows:
            for i in row:
                print(f"     -{i}")
    elif num == 9:
        break
    sleep(0.5)
stdout.write("\rSalvando Altera��es!")
sleep(1)
stdout.write("\rPrograma Finalizado!")
sleep(1)
stdout.write("\rVolte Sempre :)")
sleep(1)
stdout.write("\r   <<<   Fui   >>>")
sleep(1)
stdout.write("\r ")
sleep(0.1)
