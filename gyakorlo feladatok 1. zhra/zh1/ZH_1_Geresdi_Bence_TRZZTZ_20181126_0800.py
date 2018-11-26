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

# Geresdi Bence ZH1
#TRZZTZ

#deklarálom a listákat
datum = []
nev = []
keresztnev = []

#beolvasom a file-t, egyenesen a netről

file = urllib2.urlopen("http://www.born.nhely.hu/Python/itt_lesz_majd_az_eloZH/ez_a_zh_8/nevnap_ekezetlen.txt","r")

for line in file:
    sor = line.split(" ")
    datum.append(sor[0])
    nev.append(sor[1])
    



# eltuntetem az entereket az utolso szo vegerol
for i in range(len(nev)):
    nev[i] = nev[i][:-1]


# 1. feladat
d = 0 # számláló
for i in range(len(datum)):
    if(datum[i][0] == "1" and datum[i][1] == "1"): # ha a dátum 0. és 1. karaktere 1 akkor novemberi honapot iratom ki
        print datum[i] + " " + nev[i]
        d+=1
   
    if d == 10: # ha a szamlalo 10, akkor keri az entert
        enter = raw_input("uss entert a folytatashoz: ") 
       
        if(enter == ""):
            if(datum[i][0] == "1" and datum[i][1] == "1"):
               
                print datum[i] + " " + nev[i]
                
        else:
            break 
        
    if d == 20: # ha a szamlalo 20, akkor keri az entert 
        enter = raw_input("uss entert a folytatashoz: ") 
        if(enter == ""):
            if(datum[i][0] == "1" and datum[i][1] == "1"):
                print datum[i] + " " + nev[i]
        else:
            break # ha nem talál több novemberit, akkor kilép

print "" # sortores   

#2. feladat:




formaltdatumbe = "" # Létrehozok egy üres sztringet, amit majd kiiratok, ha hozzáfűztem az adatokat
datumbe = raw_input("kerek egy dátumot „20181126” formátumban: ") # bekérek egy dátumot

formaltdatumbe = datumbe[4] +datumbe[5]+"."+datumbe[6]+datumbe[7] #átalakítom vizsgálható formátumra(mint ami a txtben van)

str(datumbe)   #átkonvertálom sztringre
while datumbe != "X":


    #végig megyek a tombon for ciklussal
    for i in range(len(nev)):
        if formaltdatumbe == datum[i]:
            # formaltdatumbe stringnel megvizsgálom hogy mi az elso ket karakterenek a szám szerinti jelentése 01 --> Január (és ezt a többi hónapnál is végrehajtom)
            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "1"):
                print "Január " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "2"):
                print "Február " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])  

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "3"):
                print "Március " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "4"):
                print "Április " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "5"):
                print "Május " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "6"):
                print "Június " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "7"):
                print "Július " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "8"):
                print "Augusztus " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "0" and formaltdatumbe[1] == "9"):
                print "Szeptember " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "1" and formaltdatumbe[1] == "0"):
                print "Október " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "1" and formaltdatumbe[1] == "1"):
                print "November " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

            if(formaltdatumbe[0] == "1" and formaltdatumbe[1] == "2"):
                print "December " + str(formaltdatumbe[3])+str(formaltdatumbe[4])+ ": "+ str(nev[i])

    datumbe = raw_input("kerek egy dátumot „20181126” formátumban (Kilépés X lenyomásával): ")
    if datumbe == "X": #ha X et ad a felhasznalo kilep 
        break
       
    formaltdatumbe = datumbe[4] +datumbe[5]+"."+datumbe[6]+datumbe[7] #átalakítom vizsgálható formátumra(mint ami a txtben van)
    str(datumbe)   #átkonvertálom sztringre

print "" # sortores

#3. feladat: 
benev = raw_input("Kerlek adj meg egy nevet, és én megmondom mikor van a szuletesnapja(Kilépés: X): ") # bekérem a nevet
van = False #logikai változó
# while ciklussal kerem be a neveket, amig a felhasználó nem ad X-et
while benev != "X":
    
 
    for j in range(len(nev)):

        if nev[j] == benev:
            print datum[j] , " napon van ", nev[j], " születésnapja." 
            van = True # ha talált nevet, akkor igaz lesz
         
    if van == False:
        print "Nagyon sajnálom, nincs ilyen nev" # ha nem talált nevet akkor hamis marad és kiirja, h sajnos nincs ilyen nev
    benev = raw_input("Kerlek adj meg egy nevet, és én megmondom mikor van a szuletesnapja(Kilépés: X): ")
    van = False

print "" #sortores
# 4. feladat

bebetu = raw_input("Adj meg egy betűt, és én kilistázom az azzal kezdodo neveket. ") # bekérem a betut
kiir ="" #letrehozom a kiir valtozot
# for ciklussal vegig megyek a neveken
for i in range(len(nev)):
    if bebetu == nev[i][0]: # Ha olyan nevet talalok, amelynek kezdobetuje megegyezik a beirt kezdobetuvel, akkor azt hozzaadom a kiir srtingemhez
        kiir += nev[i] + ", "

print kiir #"kiiratom a neveket"