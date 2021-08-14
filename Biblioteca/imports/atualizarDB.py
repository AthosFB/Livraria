def alterar():
    import mysql.connector
    from Biblioteca.imports import leituras
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
    print("""Alterar Informação:
    [1]- Autores
    [2]- Livros""")
    while True:
        print("--" * 100)
        table = int(input("Escolha: "))
        print("--" * 100)
        if table == 1:
            validador = "idautor"
            table = "autores"
            print("""Alterar Informação:
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
                    print("\033[1;31mValor inválido!\033[1;97m")
                    print("--" * 100)
            break
        elif table == 2:
            validador = "idlivro"
            table = "livros"
            print("""Alterar Informação:
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
                    print("\033[1;31mValor inválido!\033[1;97m")
                    print("--" * 100)
            break
        else:
            print("\033[1;31mValor inválido!\033[1;97m")
            print("--" * 100)
    if item == "idautor":
        novo = leituras.intput("Coloque o novo Id Autor: ")
        print("--" * 100)
    else:
        mcursor.execute(f"select * from {table};")
        rows = mcursor.fetchall()
        if table == "autores":
            print(f"{'Nome: ':<90} {'Nacionalidade: ':>90}")
            print("--" * 100)
            for row in rows:
                for enu, i in enumerate(row):
                    if enu == 1:
                        print(f"{i:<90}", end="")
                    elif enu == 2:
                        print(f"{i:>90}")
        else:
            print(f"{'Nome: ':<90} {'Autor: ':>90}")
            print("--" * 100)
            for row in rows:
                for enu, i in enumerate(row):
                    if enu == 1:
                        print(f"{i:<90}", end="")
                    elif enu == 2:
                        print(f"{i:>90}", end="")
                print()
        print("--" * 100)
        novo = str(input("Coloque a alteração: ")).strip().title()
        print("--" * 100)
    escolhido = int(input("Coloque o id  do livro/autor que deseja alterar (9999 não sabe o id): "))
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
