import sqlite3

def hospital():
    try:
        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON;")
        cursor = conexao.cursor()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS hospitais(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       cidade TEXT NOT NULL
                       )
                       ''')
        
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS medicos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       crm TEXT NOT NULL,
                       id_hospital INTEGER,
                       FOREIGN  KEY (id_hospital) REFERENCES hospitais (id)
                       )
                       ''') 
        
        conexao.commit()

    except :
        print("Erro na tabela")

def cadastar():
     while True:
        print("1 - Cadastrar hospital")
        print("2 -  ")
