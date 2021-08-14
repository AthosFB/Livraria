def inicio():
    print("--" * 100)
    print(""" O que deseja fazer: 
     [1]- Ver Autores Cadastrados
     [2]- Ver Livros Cadastrados
     [3]- Cadastrar Novo Autor
     [4]- Cadastrar Novo Livro
     [5]- Ver Livros e seus Autores
     [6]- Procurar por Livro Especifico
     [7]- Alterar Alguma Informação
     [8]- Procurar Livros de Algum Autor
     [9]- Sair Do Programa""")
    print("--" * 100)


def fim():
    from sys import stdout
    from time import sleep
    stdout.write("\rSalvando Alterações!")
    sleep(1)
    stdout.write("\rPrograma Finalizado!")
    sleep(1)
    stdout.write("\rVolte Sempre :)")
    sleep(1)
    stdout.write("\r   <<<   Fui   >>>")
    sleep(1)
    stdout.write("\r ")
    sleep(0.1)


def mostrarautor():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
    mcursor.execute("select * from autores order by idautor;")
    rows = mcursor.fetchall()
    print(f"{'ID':<5}{'NOME':<120}{'NACIONALIDADE':>30}")
    print("--" * 100)
    for row in rows:
        for enu, i in enumerate(row):
            if enu == 0:
                print(f"{i:<5}", end="")
            elif enu == 1:
                print(f"{i:<120}", end="")
            else:
                print(f"{i:>30}")


def mostrarlivros():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
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


def escreverautorelivro():
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    mcursor.execute("use biblioteca;")
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
