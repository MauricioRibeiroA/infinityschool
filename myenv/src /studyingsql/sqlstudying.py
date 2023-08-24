from sqlite3 import Cursor
import mysql.connector

    
db_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gahega2020.',
    database='db_infiniity'
    )

cursor = db_conn.cursor()

""" CRUD """

# """ CREATE """
# nome_produto = 'chocolate'
# valor = 13
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# db_conn.commit() #necessário quando o comando edita o db

# """ READ """
# comando = F'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() #necessario quando o comando lê o db
# print(resultado)

# """ UPDATE """
# nome_produto = 'Toddynho'
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# db_conn.commit() #necessário quando o comando edita o db

# """ DELETE """
# nome_produto = 'Toddynho'
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# db_conn.commit() #necessário quando o comando edita o db
















cursor.close()
db_conn.close()