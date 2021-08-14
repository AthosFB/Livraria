def procurarlivro():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
    livro = str(input("Nome do livro: ")).title().strip()
    mcursor.execute(f"""select l.idlivro, l.nomelivro, a.nomeautor, a.nascionalidade
    from livros as l join autores as a 
    on l.idautor = a.idautor
    where nomelivro = '{livro}';""")
    rows = mcursor.fetchall()
    if len(rows) == 0:
        print("--" * 100)
        print("\033[1;31mLivro Não Cadastrado!\033[1;97m")
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


def procurarescritor():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
    from Biblioteca.imports import leituras
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
