import os 
import sys


if len(sys.argv) > 1: 
	url = str(sys.argv[1])
else:
	url = "sccd.serpro"


os.system("ping -w 1 "+url +"> teste" )

teste = open("teste","r")

result = teste.read()
campos = result.split("(")
ip,null = campos[1].split(")")

print ( "resultado do ping:", ip )

