import re
import urllib

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("2210bd88db2d50631a51f5ef9d10a28f", "bd2933699aec6b063d7f9efbd2b8843aa6a837e9b6ba31fb9dc9047dde498de7")

f = urllib.urlopen("http://www.resultados11.es/")
data = f.read()
f.close()

pattern = re.compile('<li>(\d)</li>\s*<li>(\d)</li>\s*<li>(\d)</li>\s*<li>(\d)</li>\s*<li>(\d)</li>')
premiado = pattern.findall(data)

pattern = re.compile('\d+/\d+/\d+')
fechas = pattern.findall(data)

valores = str(premiado)
valores_ok = valores.split("'")

bclient.write('dev', 'res1', valores_ok)

val1 = int(valores_ok[1])
val2 = int(valores_ok[3])
val3 = int(valores_ok[5])
val4 = int(valores_ok[7])
val5 = int(valores_ok[9])

print val1, val2, val3, val4, val5


cifra1 = int(input("introduce cifra 1: "))
while cifra1 > 9:
        cifra1 = int(input("ERROR: introduce cifra 1: "))
cifra2 = int(input("introduce cifra 2: "))
while cifra2 > 9:
        cifra2 = int(input("ERROR: introduce cifra 1: "))
cifra3 = int(input("introduce cifra 3: "))
while cifra3 > 9:
        cifra3 = int(input("ERROR: introduce cifra 1: "))
cifra4 = int(input("introduce cifra 4: "))
while cifra4 > 9:
        cifra4 = int(input("ERROR: introduce cifra 1: "))
cifra5 = int(input("introduce cifra 5: "))
while cifra5 > 9:
        cifra5 = int(input("ERROR: introduce cifra 1: "))
print("TU BOLETO="), cifra1, cifra2, cifra3, cifra4, cifra5

if cifra1 == val1 and cifra2 == val2 and cifra3 == val3 and cifra4 == val4 and cifra5 == val5:
    print("PREMIO = EL GORDO SOCIOOOOOOO")
elif cifra2 == val2 and cifra3 == val3 and cifra4 == val4 and cifra5 == val5:
    print("PREMIO = UUUUUY!! LAS CUATRO ULTIMAS")
elif cifra3 == val3 and cifra4 == val4 and cifra5 == val5:
    print("PREMIO = TRES ULTIMAS")
elif cifra4 == val4 and cifra5 == val5:
    print("PREMIO = DOBLE REINTEGRO")
elif cifra5 == val5:
    print("PREMIO = REINTEGRO")
else:
    print("OTRA VEZ SERA")


