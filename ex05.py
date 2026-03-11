codigo = int(input("qual o seu codigo do seu pacote ? "))
peso = float(input("qual o kg do seu pacote?"))
status = "entrega normal" 

if peso < 5 and codigo % 10 == 0:
    status = "entrega expressa"

if peso > 50:
    status = "entrega pesada"

print (f"pacote{codigo}: {status}")