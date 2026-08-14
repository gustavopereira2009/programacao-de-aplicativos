import sqlite3


def criar_banco_da_rede_de_hoteis():
    try:
        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()

        cursor.execute('''
               CREATE TABLE IF NOT EXISTS redes_hotel(
               id INTEGER  PRIMARY KEY AUTOINCREMENT,
               nome_rede TEXT NOT NULL,
               clasificaco_estrelas INTEGER NOT NULL                   
               )
               ''')




        cursor.execute('''
               CREATE TABLE IF NOT EXISTS hoteis(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               cidade_turistica TEXT NOT NULL,
               id_rede INTEGER NOT NULL,
               FOREIGN KEY (id_rede) REFERENCES redes_hotel (id)          
               )
               ''')
    

        conexao.commit()
        conexao.close()

    except:
        print("Erro ao cadastar banco e nas tabelas")




def cadastar_rede():
    try:
        nome = input("Digite o nome da rede de hoteis:  ")
        estrelas = int(input("Digite a quantidade de estrelas de 1 a 5: "))

        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()


        cursor.execute(
            "INSERT INTO redes_hotel (nome_rede,classificao_estrelas) VALUES"
            "(?,?)",
            (nome,estrelas), 
              )


        conexao.commit()
        conexao.close()

        print("redes cadastardas com sucesso")

    except ValueError:
        print("Digite apenas numero na estrela")

    except:
        print("Erro ao cadastar")



def listar_redes():
    try:
        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM redes_hotel ")
        redes = cursor.fetchall()
        conexao.close()


        for rede in redes:
            print("ID", rede [0])
            print("NOME:", rede [1])
            print("ESTRELAS:", rede [2])

    except:
        print("Erro ao listar redes")


def atualizar_redes():
    try:
        listar_redes()
        id_rede = int(input("Digite o id da rede que vc deseja atualizar:  "))
        novo_nome = input("Digite o novo nome da rede:  ")
        nova_estrelas = int(input("Digite quantas estrelas essa rede tem"))

        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE redes_hotel SET nome_rede = ?, classificao_estrelas = ? WHERE"
            "id = ?",
            (novo_nome, nova_estrelas, id_rede),
        )

        conexao.commit()
        conexao.close()
        print("Rede atualizada com sucesso")

    except ValueError:
        print("Digite apenas numero para o id e para as estrelas")
    except:
        print("Erro ao atualizar redes")



def excluir_rede():
    try:
        listar_redes()
        id_rede = int(input("Digite on id que vc deseja excluir"))

        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM redes_hotel WHERE id = ?,"(id_rede))

        conexao.commit()
        conexao.close()
    except ValueError:
        print("Digite apenas numero no id")
    except:
        print("Erro ao excluir rede")

    
def cadastrar_hotel():
  try:
    listar_redes()
    id_rede = int(input("digite o ID da rede de hotéis à qual este hotel pertence: "))

    conexao = sqlite3.connect("rede_hoteis.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM redes_hotel WHERE id = ?", (id_rede,))
    rede_existe = cursor.fetchone()

    if not rede_existe:
      print("Erro: O ID da rede informado não existe.")
      conexao.close()
      return

    cidade = input("Digite a cidade turística do hotel: ")

    cursor.execute(
        "INSERT INTO hoteis (cidade_turistica, id_rede) VALUES (?, ?)",
        (cidade, id_rede),
    )

    conexao.commit()
    conexao.close()
    print("Hotel cadastrado com sucesso!")
  except ValueError:
    print("Digite um número válido para o ID da rede.")
  except:
    print("Erro ao cadastrar hotel")



def listar_hoteis():
    try:
        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()


        cursor.execute("SELECT  * FROM hoteis")
        hoteis = cursor.fetchall()
        conexao.close()


        for hotel in hoteis:
         print("ID",hotel[0])
         print("Cidade",hotel[1])
         print("ID da rede",hotel[2])
    except:
        print("Erro ao listar hoteris")


def atualizar_hotel():
    try:
        id_hotel = int(input("Digite o id do hotel que voce quer alterar"))
        cidade = input("Digite o nome da cidade que voce deseja alterar")
        id_rede = int(input("digite o novo id do rede_hoteis"))

        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT id FROM redes_hotel WHERE id = ?", (id_rede,))
        rede = cursor.fetchone()


        if not rede:
            print(" ID da rede hoteleira não existente")
            conexao.close()

            return
        cursor.execute("UPDATE hoteis SET cidade_turistica = ?, id_rede = ? WHERE id = ?", (cidade, id_rede, id_hotel))
        conexao.commit()
        conexao.close()
        print("Hotel atualizado com sucesso")
    except:
        print("Erro ao atualizar hotel")


def excluir_hotel():
    try:
        id_hotel = int(input("ID do hotel que deseja excluir: "))
       
        conexao = sqlite3.connect("rede_hoteis.db")
        cursor = conexao.cursor()
        
        cursor.execute("DELETE FROM hoteis WHERE id = ?", (id_hotel,))
        
        conexao.commit()
        conexao.close()
        print("Hotel excluido com sucesso")
   
    except:
        print("Erro ao excluir hotel")



def menu():
    criar_banco_da_rede_de_hoteis()
    while True:
        try:
            print("1 Cadastrar redes de hoteis")
            print("2 Listar redes de hoteis")
            print("3 Atualizar redes de hoteis")
            print("4 Excluir redes de hotel")
            print("5 Cadstar hotel")
            print("6 Listar hoteis")
            print("7 Atualizar hoteis")
            print("8 Excluir hotel")
            print("9 sair")

            opcao = int(input("Escolha uma opcao: "))
           
            if opcao == 1:
                cadastar_rede()

            elif opcao == 2:
                listar_redes()

            elif opcao == 3:
                atualizar_redes()

            elif opcao == 4:
                excluir_rede()

            elif opcao == 5:
                cadastrar_hotel()

            elif opcao == 6:
                listar_hoteis()

            elif opcao == 7:
                atualizar_hotel()

            elif opcao == 8:
                excluir_hotel()
            
            elif opcao == 9:
                print("Saindo do sistema")
                break

                
            else:
                print("Opcaao invaliuda digite um numero de 1 a 9")

        except:
            print("Erro no menu")



menu()