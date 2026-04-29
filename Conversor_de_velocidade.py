def converter_km_para_ms(velocidade_kmh):
   
    velocidade_ms = velocidade_kmh / 3.6
    return velocidade_ms

entrada = input("Digite a velocidade em km/h: ")
velocidade_usuario = float(entrada)

if velocidade_usuario > 80:
    resultado_ms = converter_km_para_ms(velocidade_usuario)
    
    print("Velocidade em m/s:", resultado_ms)
    print("Reduza a velocidade!")
else:
    print("Velocidade dentro do limite permitido.")