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



#bekeres easyguival

benev=enterbox(msg="Kerek egy keresztnevet(0-val kilepes):")
bepont=enterbox(msg="Kerek egy pontszamot(0-val kilepes):")

# file letrehozas kiiratashoz (hozzafuzes): 
file = open("szomoru.txt", "a")
for i in range(len(vidam)):
    file.write(szomoru[i] + ", ")
file.close()

# Kulso fajl megnyitasa adat beolvasasra
file = open("kulsoFajl.txt","r")

# Kulso fajl megnyitasa adat kiiratasra( torli az eddigi tartalmat)
file = open("kulsoFajl.txt","w")

#kulso file megnyitasa(url)
file = urllib2.urlopen("http://www.born.nhely.hu/Python/Gyakorlo_feladatsor_2018_11_12/hol.txt","r")
for line in file:
    sor = line.split()
    tomb.append(sor)


# tomb random eleme
random.choice(tomb)


# int tomb novelese:

tomb.append(2)

#string tomb novelese:

tomb += "bele"