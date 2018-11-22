# coding: utf-8

'''
http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/Gyakorlo_felad
atsor_20181112.pdf

1. Készítsen egy programot, amely addig olvas be vidám (mosolygós, nevetős,
pl. :), :-),    stb.) smiley-kat egy listába, amíg a felhasználó nem visz be
üres stringet (üres Enter). Ezután kérjen egy másik listába negatív (szomorú,
mérges stb.) arcokat. Végül írja ki a megismert smiley-kat a képernyőre!

2. Bővítse az 1. feladatot úgy, hogy a megismert smiley-kat írja ki két
fájlba is: smiley_pozitiv.txt és smiley_negativ.txt.

3. Készítsen chat-generátor programot, amely megadott szavakból állítja össze
egy beszélgetés (chat) 30 véletlenszerű mondatát. A felhasználható elemek
ezekben a fájlokban találhatók: ki_mondja.txt, ki.txt, kivel.txt mikor.txt
hol.txt mit_csinalt.txt. Minden mondat végét az előző feladatban elkészített
smiley-fájl 1-1 eleme zárja. A mondatok szerkezete mindig ilyen legyen:<Ki
mondja>: <Ki> <kivel> <mikor> <hol> <mit csinált>. (Ha nem sikerült
megoldania a 2. feladatot, akkor használja a megadott smiley_pozitiv.txt és
smiley_negativ.txt fájlokat.) A mondatokat írja ki képernyőre.

4. Bővítse a 3. feladatban megírt programot úgy, hogy az elkészített
beszélgetést mentse el egy chat.txt nevű fájlba. Készítsen programot, amely
elemzi az így elmentett fájlt. (Ha nem sikerült megoldania a 3. feladatot,
akkor használja a megadott chat.txt fájlt.) A program a mondatok végén
elhelyezett smiley-k alapján mondja meg, hogy ki milyen lelkiállapotban van.  
(A hozzászólók pontokat kapnak a mondatuk végén található smiley-k után,
minden pozitív smiley után +1-et, minden negatív smiley után -1-et.) Írja ki
a résztvevők listáját és vidámság-pontszámát, csökkenő sorrendben.

'''

import urllib
from random import choice as rc # random.choice(list) helyett: rc(list)

# Ez a függvény fogja beolvasni a fájlokat, és előkészíteni a listákat
def urlBeolvas(fajl):
    urlPath = "http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/"
    kim = urllib.urlopen(urlPath + fajl)
    lista = kim.read().split("\n")
    #print lista
    kml = []
    for km in lista:
         #print km
         km = km[:-1] # a sorok végén volt egy "\r" karakter
         #print km
         kml.append(km)
    kml = kml[:-1] # a fájl végén is volt egy Enter
    return kml


# Tesztelés során az alábbi blokk megjegyzésbe tehető, és a lentebbi két értékadás segít  
vidamLista = []
vidam = raw_input("Kérek egy vidám smiley-t. (Üres Enter: vége.) - ")
while vidam != "":
    vidamLista.append(vidam)
    vidam = raw_input("Kérek egy vidám smiley-t. (Üres Enter: vége.) - ")

szomoruLista = []
szomoru = raw_input("\nKérek egy szomorú smiley-t. (Üres Enter: vége.) - ")
while szomoru != "":
    szomoruLista.append(szomoru)
    szomoru = raw_input("Kérek egy vidám smiley-t. (Üres Enter: vége.) - ")


# Tesztelés során a fenti blokk helyett ez a két sor legyártja a két listát:
### vidamLista = [":))",":D",":)"]
### szomoruLista = [":[",":{"]

print "\nA vidám lista: ", vidamLista
print "A szomorú lista: ", szomoruLista, "\n"

vid = open("smiley_pozitiv.txt", "a+")
for v in vidamLista:
    vid.write(v + "\n")
vid.close()

szom = open("smiley_negativ.txt", "a+")
for sz in szomoruLista:
    szom.write(sz + "\n")
szom.close()


kimLista = urlBeolvas("ki_mondja.txt")
#print kimLista

kiLista = urlBeolvas("ki.txt")
#print kiLista

kivelLista = urlBeolvas("kivel.txt")
#print kivelLista

mikorLista = urlBeolvas("mikor.txt")
#print mikorLista

holLista = urlBeolvas("hol.txt")
#print holLista

mitLista = urlBeolvas("mit_csinalt.txt")
#print mitLista


'''
google: random choice from list:
https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
random.choice(list)
'''

chatStr = ""

for mondat in range(30):
    chatStr += rc(kimLista) + ": " + rc(kiLista) + " " + rc(kivelLista) + " " + rc(mikorLista) + " " + rc(holLista) + " " + rc(mitLista) + ". " + rc( rc( [vidamLista, szomoruLista] ) ) + "\n"

print chatStr


chatFile = open("chat.txt","w+") # w+ - ?
chatFile.write(chatStr)
chatFile.close()

'''
A program a mondatok végén elhelyezett smiley-k alapján mondja meg, hogy ki
milyen lelkiállapotban van.  (A hozzászólók pontokat kapnak a mondatuk végén
található smiley-k után, minden pozitív smiley után +1-et, minden negatív
smiley után -1-et.) Írja ki a résztvevők listáját és vidámság-pontszámát,
csökkenő sorrendben.
'''

chatList = chatStr.split("\n")
#print chatList

Peti = Pali = Zita = Inez = Zsuzsi = 0 # vidámság-számláló

# pontozás

for actualSentence in chatList:
    words = actualSentence.split(" ")
    if words != ['']: # kiszűröm a fájl végén lévő üres sort
         #print words
         if words[6] in vidamLista: # ha vidám mondat
              pont = 1				# +1
         elif words[6] in szomoruLista:
              pont = -1
         else:
              pont = 0
              print "Baj van <<<<<<<"

         if words[0] == "Peti:":
              # print "Peti megvan"
              Peti += pont
         elif words[0] == "Pali:":
              # print "Pali megvan"
              Pali += pont
         elif words[0] == "Zita:":
              # print "Zita megvan"
              Zita += pont
         elif words[0] == "Inez:":
              # print "Inez megvan"
              Inez += pont
         elif words[0] == "Zsuzsi:":
              # print "Zsuzsi megvan"
              Zsuzsi += pont

# csökkenő sorrendben!

#pontok = [Peti, Pali, Zita, Inez, Zsuzsi]
''' 
Lehetne szépen, kőbaltás módszerrel:
- pontok = pontok.sort(reverse=True)
- végigmenni a pontok listáján
- megkeresni a hozzá tartozó nevet (egyezés nem gond)
- kírni

'''


# További tippek:
# - https://stackoverflow.com/questions/17555218/python-how-to-sort-a-list-of-lists-by-the-fourth-element-in-each-list
#   nevekPontok = nevekPontok.sort(reverse = True, key = lambda x: int(x[1]) )
# - Barnabás megoldása: valami pointer...


nevekPontok = [["Peti",Peti], ["Pali",Pali], ["Zita",Zita], ["Inez", Inez], ["Zsuzsi",Zsuzsi] ]

# print "eredeti nevekPontok:\n", nevekPontok
nevekPontok = sorted(nevekPontok, reverse = True, key = lambda x: int(x[1]))
# print "sorbarendezett nevekPontok:\n", nevekPontok

# Kiírás pontszám szerint rendezve, a legnagyobbal kezdve:
for i in range(5):
	print "%6s:   %3d" % (nevekPontok[i][0], nevekPontok[i][1])

	# na, itt tűnt fel, hogy szebb lett volna, ha ezt a nevekPontok listát már a pontozásnál is használjuk...
