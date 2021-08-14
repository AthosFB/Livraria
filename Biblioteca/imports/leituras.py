def intput(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            print("\033[1;31mO usuario preferiu não informar o valor!!!\033[m")
        except:
            print("\033[1;31mValor Inválido")
            print("Tente Novamente!!!\033[1;97m")
        else:
            break
    return a


def lerlivro():
    from Biblioteca.imports.Backup import escrever
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
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
    print("Se o autor não estiver cadastrado (7777)")
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
        arq = "Backup.txt"
        escrever(arq, nomelivro, nomedoautorBackup)
        mcursor.execute(f"insert into livros value (default, '{nomelivro}', '{idautor}')")


def lerautor():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
    nomeautor = str(input("Nome do autor: ")).title().strip()
    print("--" * 100)
    nascionalidade = str(input("País de nascionalidade do autor: ")).title().strip()
    print("\033[1;32mAutor Cadastrado Com Sucesso!\033[1;97m")
    mcursor.execute(f"insert into autores value (default, '{nomeautor}', '{nascionalidade}')")
