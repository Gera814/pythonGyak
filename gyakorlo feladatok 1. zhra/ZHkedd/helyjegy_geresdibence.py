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

#listak letrehozasa
ules = []
kezd_km = []
veg_km = []


# beolvasom a txt filet
file = open("eladott.txt","r")

#feltoltom a listakat
for line in file:
    sor = line.split(" ")
    ules.append(sor[0])
    kezd_km.append(sor[1])
    veg_km.append(sor[2])

# eltuntetem az entereket az utolso szo vegerol
for i in range(len(veg_km)):
    veg_km[i] = veg_km[i][:-1]


# 2. feladat:

max = len(ules)
print "2. feladat : A legutolsó jegyvásárló ülésének száma, utázás hoszza(km): ",ules[max-1], ", ", int(veg_km[max-1])-int(kezd_km[max-1]), " km"

# 3. feladat: 
vegigutazok = []
for i in range(len(ules)):
    if int(veg_km[i]) - int(kezd_km[i]) == 200:
        vegigutazok.append(ules[i])

print "3. feladat : végigutazok sorszama: ", vegigutazok[0]

# 4. feladat: 
km = 0
for i in range(len(ules)):
    km +=  ((int(veg_km[i]) - int(kezd_km[i])) / 10) * 71

print "4. feladat bevetel: ", km

#5. feladat:
'''
db = 0
for i in range(len(ules)):
    if (int(kezd_km[i]) == max(int(kezd_km))):
        db+=1

print "5. feladat: utolso felszallok szama: ", db
'''
for line in range(1,11):
    for table in range(1,11):
        print line * table, '\t',
    print 
