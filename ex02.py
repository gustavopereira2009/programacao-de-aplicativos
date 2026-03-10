ano = int(input("Qual o ano"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 4):
    print(f"O ano {ano} e bissexto")
else:
    print(f" O ano {ano} e um comum")