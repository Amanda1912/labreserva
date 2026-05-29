import sqlite3

DB_NAME = "reservas.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            professor TEXT NOT NULL,
            email TEXT NOT NULL,
            laboratorio TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL,
            disciplina TEXT NOT NULL,
            UNIQUE(laboratorio, data, horario)
        )
    """)

    conexao.commit()
    conexao.close()