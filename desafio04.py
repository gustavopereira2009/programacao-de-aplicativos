drone = int(input ("qual o codigo do drone? "))
autorizacao = input("voce possui autorizacao (s/n)")

if drone == 999 or autorizacao == "s":
  print("autorizacao concedida")
else:
   print("ERRO 01: drone nao identificado. Retornando a base")

bateria = int(input("qual o nivel da bateria de ( 0 a 100)?:"))
clima = input("o clima deve estar (ensolarado/chuvosos):")
velocidade = float(input("a velocidade do vento em (km/h):"))

if bateria < 10:
        print("o pouso deve ser AUTORIZADO IMEDIATAMENTE por seguranca")

else:
      if (clima == "ensolarado" and velocidade <=30) or (clima == "chuvoso" and velocidade <=10):
           print("pouso autorizado")
      else:
           print("pouso negado, por motivos de clima")