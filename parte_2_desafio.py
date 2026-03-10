garrafas = int(input("Digite o número total de garrafas que já passaram pela esteira hoje: "))

# Regras de negócio
if garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")
    print("QUALIDADE: Retirar amostra para teste.")
elif garrafas % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")
else:
    print(f"Produção em dia. Garrafa número {garrafas} processada.")