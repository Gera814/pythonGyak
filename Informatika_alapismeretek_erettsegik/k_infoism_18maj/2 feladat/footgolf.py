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


'''
Geresdi Bence
informatika alapismeretek erettségi 2018 majus
'''
# létrehozom a listákat az adatoknak
nev = []
kateg = []
egyesulet = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
versenyzodb = 0


file= open("fob2016.txt", "r")

for line in file:
    mondat = line.split(";")
    nev.append(mondat[0])
    kateg.append(mondat[1])
    egyesulet.append(mondat[2])
    p1.append(mondat[3])
    p2.append(mondat[4])
    p3.append(mondat[5])
    p4.append(mondat[6])
    p5.append(mondat[7])
    p6.append(mondat[8])
    p7.append(mondat[9])
    p8.append(mondat[10])
    versenyzodb+=1
    
# eltuntetem az entereket az utolso szo vegerol
for i in range(7):
    p8[i] = p8[i][:-1]

print "3. feladat: versenyzok szama :", versenyzodb


# 4. feladat
noidb = 0
for i in range(versenyzodb):
    if kateg[i] == "Noi":
        noidb+=1
       
float(noidb)
float(versenyzodb)
print "4. feladat: A női versenyzők aránya: ", float((noidb*100)/versenyzodb), "%."

# 5. feladat (fuggveny)


def soronkent(i,sor):
        sor.append(int(p1[i]))
        sor.append(int(p2[i]))
        sor.append(int(p3[i]))
        sor.append(int(p4[i]))
        sor.append(int(p5[i]))
        sor.append(int(p6[i]))
        sor.append(int(p7[i]))
        sor.append(int(p8[i]))
        
        sor = [z for z in sor if z != 0] # kiszedem a nullákat
        db = 0
       
        if(min(sor) != max(sor)): # megnézem hogy a legnagyobb elem egyenlő e a legkissebbel, mert ha igen akkor nem törlök elemet hanem csak osszegzek
                sor.remove(min(sor))
                db+=1
        if(min(sor) != max(sor)):
                sor.remove(min(sor))
                db+=1
        if(db == 1):
                sor.append(10)
        if(db == 2):
                sor.append(10)
                sor.append(10)
               

        print  nev[i], sor
        print sum(sor)

elsosor = []
soronkent(0,elsosor)

masodiksor = []
soronkent(1,masodiksor)
#for i in range(len(nev)):
       # soronkent(i,soksor[i])




        

