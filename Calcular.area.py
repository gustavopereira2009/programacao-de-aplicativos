def calcular_area(largura, comprimento):
    area = largura * comprimento
    return area

contador = 1

print("--- Calculadora de Área de Terrenos ---")
while contador <= 3:
    print(f"\nTerreno {contador}:")
    
    largura = float(input("Digite a largura (m): "))
    comprimento = float(input("Digite o comprimento (m): "))
    
    area_final = calcular_area(largura, comprimento)
    print(f"A área do terreno {contador} é: {area_final}m²")
    
    contador += 1

print("Cálculos finalizados.")