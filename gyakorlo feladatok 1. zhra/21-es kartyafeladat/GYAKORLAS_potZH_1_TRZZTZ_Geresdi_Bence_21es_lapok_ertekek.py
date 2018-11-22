#!usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import string
from easygui import *
import easygui
import math
import random 
from random import *
import urllib2

# Geresdi Bence
# Neptun: TRZZTZ
# Feladatok : 1-4

'''
1. feladat (10 pont)
Hozzon létre két listát, amely a játékhoz szükséges adatokat (lapokat és értékeket) tárolja.
Ezután írassa ki az összes lapot és zárójelben az értékét az alábbi formában:
VII (7), VIII (8), IX (9), X (10), Alsó (2), Felső (3), Király (4), Ász (11)

2. feladat (20 pont)
A program adjon két-két véletlen lapot mind a négy játékosnak (Kati, Zsuzsi, Peti, Pali).
Írja ki az alábbi formában (a pontszámokat helyiérték szerint igazítva) a játékosok pillanatnyi állását:
Kati:	6	Alsó, Király
Zsuzsi:	18	VII, Ász
Peti:	17	IX, VIII
Pali:	10	Felső, VII

3. feladat (20 pont)
Bővítse a feladatot, kérdezze meg a program minden egyes játékostól sorban (és aztán majd további körökben), 
hogy kér-e még lapot. Aki kér, annak adjon egy-egy véletlen lapot. (Végtelen számú paklival dolgozunk, a lapok nem fogynak el.) 
Minden egyes kör után írja ki a játék állását, mint a 2. lépésben.

4. feladat (10 pont)
Hirdesse ki a program, hogy ki esett ki (akinek 21-nél több pontja van), illetve ki nyerte a játékot (akinek legtöbb, de 22-nél kevesebb pontja van). 
(A valós játékban a két ász értékesebb, mint az éppen 21 pont, plusz pontért ezt is beleveheti az értékelésbe.)
'''

# deklaralom a tomboket
kati = []
zsuzsi = []
peti = []
pali = []

# feltoltom a lap és az ertek tombokat
lap = ["VII", "VIII", "IX", "X", "Also", "Felso", "Kiraly", "Asz"]
ertek = [7, 8, 9, 10, 2, 3, 4, 11]

#kiiratom a feltoltott tomboket a minta szerint
for i in range(8):
    print str(lap[i]) + "(" + str(ertek[i]) + "), ",
    
print " "

# a szereplokhoz veletlenszeruen rendelek ket lapot es egy tombbe rakom ezeket
kati += sample(lap,1)
kati += sample(lap,1)
zsuzsi += sample(lap,1)
zsuzsi += sample(lap,1)
peti += sample(lap,1)
peti += sample(lap,1)
pali += sample(lap,1)
pali += sample(lap,1)

#kiszamolom mennyit er egy szereplo ket lapja, amit kapott
katilapertek = ertek[lap.index(kati[0])] + ertek[lap.index(kati[1])]
zsuzsilapertek = ertek[lap.index(zsuzsi[0])] + ertek[lap.index(zsuzsi[1])]
petilapertek = ertek[lap.index(peti[0])] + ertek[lap.index(peti[1])]
palilapertek = ertek[lap.index(pali[0])] + ertek[lap.index(pali[1])]

#kiiratom a szereplok ket lapjat és az erteket
print "______________________"
print "Kati: " +  str("{:8}".format(katilapertek)) + " " + str("{:3}".format(kati[0])) + ", " + str(kati[1])
print "Zsuzsi: " + str("{:6}".format(zsuzsilapertek))  + " " + str("{:3}".format(zsuzsi[0])) + ", " + str(zsuzsi[1])
print "Peti: " +  str("{:8}".format(petilapertek)) + " " + str("{:3}".format(peti[0])) + ", " + str(peti[1])
print "Pali: " +  str("{:8}".format(palilapertek)) + " " + str("{:3}".format(pali[0])) + ", " + str(pali[1])
print "______________________"

#Mindegyik szereplő két pontszámát tartalmazó stringek, később ezeket bővítem a lapokkal ha szeretnenek meg kerni.(az eddigi 2 lapon kivul)

katistringje = str(kati[0]) + ", " + str(kati[1])
zsuzsistringje = str(zsuzsi[0]) + ", " + str(zsuzsi[1])
petistringje = str(peti[0]) + ", " + str(peti[1])
palistringje = str(pali[0]) + ", " + str(pali[1])


'''
megkerdezem a szereploket egyesevel, hogy kernek e meg lapot. ha kernek akkor bovitem a fentebb letrehozott stringjuket egy lappal. 
A lapertekuket is bovitem a bovitett lap ertekenek megfelelően.
a kap
'''


katilap_3 = raw_input("Kati ker meg lapot? (igen/nem) (Ha egyszer nemet mondasz, akkor már nem kérhetsz többet!): ") 
for i in range(2, 100):
    
    if katilap_3 == "igen":
        kati += sample(lap,1) #bovitem egy lappal kati listat
        katilapertek += ertek[lap.index(kati[i])] # novelem a lap erteket, az ujonnan kert lap ertekevel
        katistringje += ", " +str(kati[i]) #kiiratashoz szukseges stringhez is hozzafuzom a kati uj lapjat --> for 2 től indul, mivel már alapból van két lapja --> kati[0] kati[1] foglalt

    zsuzsilap_3 = raw_input("Zsuzsi ker meg lapot? (igen/nem) (FONTOS !! Ha egyszer nemet mondasz, akkor már nem kérhetsz többet!): ") 
    if zsuzsilap_3 == "igen":
        zsuzsi += sample(lap,1)
        zsuzsilapertek += ertek[lap.index(zsuzsi[i])]
        zsuzsistringje += ", " +str(zsuzsi[i])

    petilap_3 = raw_input("Peti ker meg lapot? (igen/nem) (FONTOS !! Ha egyszer nemet mondasz, akkor már nem kérhetsz többet!): ") 
    if petilap_3 == "igen":
        peti += sample(lap,1)
        petilapertek += ertek[lap.index(peti[i])]
        petistringje += ", " +str(peti[i])

    palilap_3 = raw_input("Pali ker meg lapot? (igen/nem) (FONTOS !! Ha egyszer nemet mondasz, akkor már nem kérhetsz többet!): ") 
    if palilap_3 == "igen":
        pali += sample(lap,1)
        palilapertek += ertek[lap.index(pali[i])]
        palistringje += ", " + str(pali[i])
    print "\n"
    print "\n"
    print "\n"
    print "\n" 
    print i , ". edik fordulo eredmenyei:"   
    print "______________________"
    
    print "Kati: " + str("{:8}".format(katilapertek))+ " " + katistringje
    print "Zsuzsi: " +  str("{:6}".format(zsuzsilapertek)) + " " + zsuzsistringje
    print "Peti: " +  str("{:8}".format(petilapertek)) + " " + petistringje
    print "Pali: " +  str("{:8}".format(palilapertek)) + " " + palistringje
    print "______________________"
    print "\n"
    print "\n"
    print "\n"
    print "\n"
    print "::::::::::::::::", (i+1) , ". fordulo kovetkezik :::::::::::::::::\n"
    katilap_3 = raw_input("(0 lenyomásával játék vége) \n \n Kati ker meg lapot? (igen/nem) (FONTOS !! Ha egyszer nemet mondasz, akkor már nem kérhetsz többet!) : ") 
    if katilap_3 == "0":
        break
print "\n"
print "eredmenyhirdetes:"

lapertekek = []
van_nyertes = False

if katilapertek <= 21:
    lapertekek.append(katilapertek)
    i+=1 
else:
    print "kati kiesett" 

if zsuzsilapertek <= 21:
    lapertekek.append(zsuzsilapertek)
    i+=1  
else:
    print "zsuzsi kiesett" 


if petilapertek <= 21:
    lapertekek.append(petilapertek)
    i+=1 
else:
    print "peti kiesett" 


if palilapertek <= 21:
    lapertekek.append(palilapertek)
else:
    print "pali kiesett" 

if van_nyertes == False:
    max = 0

    for i in range(len(lapertekek)):
        if max < lapertekek[i]:
            max = lapertekek[i]
if max == petilapertek:
    print "A nyertes: Peti"

if max == zsuzsilapertek:
    print "A nyertes: Zsuzsi"

if max == palilapertek:
    print "A nyertes: Pali"

if max == katilapertek:
    print "A nyertes: Kati"


    

    




