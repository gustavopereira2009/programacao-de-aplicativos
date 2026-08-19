def eh_par(numero):
    return numero % 2 == 0


assert eh_par(4) == True, "Deveria ser True para o numero 4"

assert eh_par(3) == False, "Deveria ser false para o numero 3"

assert eh_par(0) == True, "Deveria ser True para o numero 0"

assert eh_par(-2) == True, "Deveria ser True para o numero -2"


print("Todos os teste foram feitos")