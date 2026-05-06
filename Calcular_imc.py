def calcular_imc (nome,peso,altura,idade):
     return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    else:
        if imc < 25:
            return "Normal"
        else:
            if imc < 30:
                return "Sobrepeso"
            else:
                return "Obesidade"

def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = calcular_imc(peso, altura)
    categoria = classificar_imc(imc)
    relatorio = nome + ", com " + (idade) + " anos, seu IMC é " + \
                ("%.2f" % imc) + " e sua classificação é: " + categoria + "."
    return relatorio


nome_usuario = input("Digite seu nome: ")
peso_usuario = float(input("Digite seu peso em kg: "))
altura_usuario = float(input("Digite sua altura em metros: "))
idade_usuario = int(input("Digite sua idade: "))


resultado = gerar_relatorio_saude(nome_usuario, peso_usuario, altura_usuario, idade_usuario)


print("--- Relatório de Saúde ---")
print(resultado)