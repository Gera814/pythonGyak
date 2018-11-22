#!usr/bin/python
# -*- coding: utf-8 -*-

#Geresdi Bence 
#Neptun: TRZZTZ

import urllib
import string
from easygui import *
import easygui
import math
import random 
from random import *
import urllib2

# listak letrehozasa
hol = []
ki = []
kimondja = []
kivel = []
mikor = []
mitcsin = []
smiley = []
#feltoltom a listakat egyesevel:
#-------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/hol.txt","r")
for line in file:
    sor = line.split()
    hol.append(sor)
    
file.close()
# ---------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/ki.txt","r")
for line in file:
    sor = line.split()
    ki.append(sor)
file.close()  
#-----------------------------------------------  
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/ki_mondja.txt","r")
for line in file:
    sor = line.split()
    kimondja.append(sor)
    
file.close()
#-------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/kivel.txt","r")
for line in file:
    sor = line.split()
    kivel.append(sor)
    
file.close()
#---------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/mikor.txt","r")
for line in file:
    sor = line.split()
    mikor.append(sor)
    
file.close()
#-------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/mit_csinalt.txt","r")
for line in file:
    sor = line.split()
    mitcsin.append(sor)
    
file.close()
#-------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/smiley_pozitiv.txt","r")
for line in file:
    sor = line.split()
    smiley.append(sor)
    
file.close()
#------------------------------------------------
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/smiley_negativ.txt","r")
for line in file:
    sor = line.split()
    smiley.append(sor)
    
file.close()


#VÉGE A LISTA FELTÖLTÉSNEK

file = open("chat_out.txt", "w")


# kiirom a 30 sort a minta szerint a chat_out.txt fileba


for i in range(30):
  file.write(sample(kimondja,1)[0][0] + ": " + sample(ki,1)[0][0] +" " + sample(kivel,1)[0][0] + " " + sample(mikor,1)[0][0] + " " + 
  sample(hol,1)[0][0] + " " + sample(mitcsin,1)[0][0] + " " +  sample(smiley,1)[0][0] + "\n")



file.close()

file = open("chat_out.txt", "r")

_kimondja = []
_ki = []
_kivel = []
_mikor = []                         #a kiirt adatokat beolvasom ujabb tombokbe, hogy tudjak velük dolgozni
_hol = []
_mitcsin = []
_smiley = []


# feltoltom az uj tombjeimet
for line in file:
  szo = line.split(" ")
  _kimondja.append(szo[0])
  _ki.append(szo[1])
  _kivel.append(szo[2])
  _mikor.append(szo[3])
  _hol.append(szo[4])
  _mitcsin.append(szo[5])
  _smiley.append(szo[6])

# változok amik szamoljak hany vidam smileyja volt az illetőnek
zsuzsi = 0 
peti = 0
pali = 0                      
zita = 0
inez = 0

#megvizsgálom egyesévle a sorokat (for), hogy melyikben van vidam smiley. ha van akkor azt a nevet novelem, amelyiknél előfordul

for i in range(len(_kimondja)):
  if _kimondja[i] == "Zsuzsi:" and (_smiley[i] == ":)\n" or _smiley[i] == ":D\n" or _smiley[i] == ":-)\n" or _smiley[i] == ":]\n" or _smiley[i] == ":-]\n")  :
    zsuzsi += 1

  if _kimondja[i] == "Peti:" and (_smiley[i] == ":)\n" or _smiley[i] == ":D\n" or _smiley[i] == ":-)\n" or _smiley[i] == ":]\n" or _smiley[i] == ":-]\n")  :
    peti += 1
  
  if _kimondja[i] == "Pali:" and (_smiley[i] == ":)\n" or _smiley[i] == ":D\n" or _smiley[i] == ":-)\n" or _smiley[i] == ":]\n" or _smiley[i] == ":-]\n")  :
    pali += 1
  
  if _kimondja[i] == "Zita:" and (_smiley[i] == ":)\n" or _smiley[i] == ":D\n" or _smiley[i] == ":-)\n" or _smiley[i] == ":]\n" or _smiley[i] == ":-]\n")  :
    zita += 1
  
  if _kimondja[i] == "Inez:" and (_smiley[i] == ":)\n" or _smiley[i] == ":D\n" or _smiley[i] == ":-)\n" or _smiley[i] == ":]\n" or _smiley[i] == ":-]\n")  :
    inez += 1
     
file.close()


# teszt kiiratas
print "Itt láthatő kinek hány vidám smiley-ja van: "
print "Zsuzsi db: ", zsuzsi
print "peti db: ", peti
print "Pali db: ", pali
print "Zita db: ", zita
print "Inez db: ", inez

#listaba teszem a neveket es a hozzajuk tartozo smilye-ik darabszamat
lista = [zsuzsi, peti, pali, zita, inez]
nevek = ["Zsuzsi", "Peti", "Pali", "Zita", "Inez"]
 
#rendezes for ciklussal
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i] < lista [j]:
            lista[i], lista[j] = lista[j], lista[i]
            nevek[i], nevek[j] = nevek[j], nevek[i]

#sorbarendezett listak
print "sorbarendezve: "
print lista
print nevek    

# file végére is kiiratom
file = open("chat_out.txt","a")
file.write("Smiley-k száma:\n")
for i in range (len(lista)):
  file.write(str(nevek[i]) + " "+ str(lista[i]) + "db" + "\n")
       
file.close()