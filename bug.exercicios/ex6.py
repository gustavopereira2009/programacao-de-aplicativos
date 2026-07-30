import sqlite3

def  buscar_professorers(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professorers WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()


    # O Python gera esse erro porque o parâmetro (id_prof) sem uma vírgula não é reconhecido como uma tupla, fazendo com que o SQLite conte as letras do ID em vez de ler o valor como um único argumento