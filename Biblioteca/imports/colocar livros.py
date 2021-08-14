import pyautogui as gui
import pyperclip as clip
import pandas as pd
livros = pd.read_excel(r"C:\Users\athos\Downloads\livros.xls")
autores = livros["Autor"]
livros = livros["Obra"]
"""for autor in autores:
    for livro in livros:
        print(f"{autor}   ---   {livro}")
        break"""
for c in range(1, 713):
    if str(autores[c]) == "nan" and str(livros[c]) == "nan":
        print(end="")
    else:
        print(f"{autores[c]}   ---   {livros[c]}")
''