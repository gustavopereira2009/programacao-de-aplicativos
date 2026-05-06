def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    if possui_certificacao == True:
        return True
    elif nota_teste > 80 and anos_xp > 2:
        return True
    else:
        return False

print("--- Sistema de Seleção de RH ---")

nota = float(input("Digite a nota técnica (0-100): "))
experiencia = int(input("Digite os anos de experiência: "))
certificacao_input = input("Possui certificação? (sim/nao): ")

if certificacao_input == "sim":
    tem_certificado = True
else:
    tem_certificado = False

aprovado = verificar_aprovacao(nota, experiencia, tem_certificado)

if aprovado == True:
    print("Resultado: Contratar")
else:
    print("Resultado: Descartar")