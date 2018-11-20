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


# deklaralom a tomboket
kati = []
zsuzsi = []
peti = []
pali = []

# feltoltom a lap és az ertek tombokat
lap = ["VII", "VIII", "IX", "X", "Also", "Felso", "Kiraly", "Asz"]
ertek = [7, 8, 9, 10, 2, 3, 4, 11]

#kiiratom a feltoltott tomboket a minta szerint

print(
str(lap[0]) + "(" + str(ertek[0]) + "), " + 
str(lap[1]) + "(" + str(ertek[1]) + "), " + 
str(lap[2]) + "(" + str(ertek[2]) + "), " + 
str(lap[3]) + "(" + str(ertek[3]) + "), " + 
str(lap[4]) + "(" + str(ertek[4]) + "), " + 
str(lap[5]) + "(" + str(ertek[5]) + "), " + 
str(lap[6]) + "(" + str(ertek[6]) + "), " + 
str(lap[7]) + "(" + str(ertek[7]) + ") ")

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
print "Kati: " +  str(katilapertek) + " " + str(kati[0]) + ", " + str(kati[1])
print "Zsuzsi: " +  str(zsuzsilapertek) + " " + str(zsuzsi[0]) + ", " + str(zsuzsi[1])
print "Peti: " +  str(petilapertek) + " " + str(peti[0]) + ", " + str(peti[1])
print "Pali: " +  str(palilapertek) + " " + str(pali[0]) + ", " + str(pali[1])
print "______________________"

# bekerem a 3. lapot:

katistringje = str(kati[0]) + ", " + str(kati[1])
zsuzsistringje = str(zsuzsi[0]) + ", " + str(zsuzsi[1])
petistringje = str(peti[0]) + ", " + str(peti[1])
palistringje = str(pali[0]) + ", " + str(pali[1])

katilap_3 = raw_input("Kati ker meg lapot? (igen/nem): ") 
for i in range(2, 100):
    
    if katilap_3 == "igen":
        kati += sample(lap,1)
        katilapertek += ertek[lap.index(kati[i])]
        katistringje += ", " +str(kati[i]) 

    zsuzsilap_3 = raw_input("Zsuzsi ker meg lapot? (igen/nem): ") 
    if zsuzsilap_3 == "igen":
        zsuzsi += sample(lap,1)
        zsuzsilapertek += ertek[lap.index(zsuzsi[i])]
        zsuzsistringje += ", " +str(zsuzsi[i])

    petilap_3 = raw_input("Peti ker meg lapot? (igen/nem): ") 
    if petilap_3 == "igen":
        peti += sample(lap,1)
        petilapertek += ertek[lap.index(peti[i])]
        petistringje += ", " +str(peti[i])

    palilap_3 = raw_input("Pali ker meg lapot? (igen/nem): ") 
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
    
    print "Kati: " + str(katilapertek)+ " " + katistringje
    print "Zsuzsi: " +  str(zsuzsilapertek) + " " + zsuzsistringje
    print "Peti: " +  str(petilapertek) + " " + petistringje
    print "Pali: " +  str(palilapertek) + " " + palistringje
    print "______________________"
    print "\n"
    print "\n"
    print "\n"
    print "\n"
    print "::::::::::::::::", (i+1) , ". fordulo kovetkezik :::::::::::::::::"
    katilap_3 = raw_input("Kati ker meg lapot? (igen/nem): ") 
    if katilap_3 == "nem":
        break

print "eredmenyhirdetes:"

lapertekek = []

if katilapertek < 21:
    lapertekek.append(katilapertek)
    i+=1
elif katilapertek == 21:
    print "katinyert"  
else:
    print "kati vesztes" 

if zsuzsilapertek < 21:
    lapertekek.append(zsuzsilapertek)
    i+=1
elif zsuzsilapertek == 21:
    print "zsuzsinyert"  
else:
    print "zsuzsi vesztes" 


if petilapertek < 21:
    lapertekek.append(petilapertek)
    i+=1
elif petilapertek == 21:
    print "peti nyert"  
else:
    print "peti vesztes" 


if palilapertek < 21:
    lapertekek.append(palilapertek)
elif palilapertek == 21:
    print "pali nyert"  
else:
    print "pali vesztes" 

max = lapertekek[0]
for i in range(len(lapertekek)):
    if max < lapertekek[i]:
        max = lapertekek[i]

print "A legnagyobb pontszamu jatekos: ", max






