from sqlite3 import Cursor
import mysql.connector
from tkinter import *

windows = Tk()
    
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gahega2020.',
    database='school_db'
    )

cursor = conexao.cursor()

""" CREATE """
tabela = 'alunos'
nome = 'joao'
idade = 27
endereco = 'salvador'

comando = f'INSERT INTO alunos (nome, idade, endereco) VALUES ("{nome}", {idade}, "{endereco}")'
cursor.execute(comando)
conexao.commit() #necessário quando o comando edita o db























cursor.close()
conexao.close()