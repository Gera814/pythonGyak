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

#:::::::::::::::::::::::::::::::::::::::::::::::::::::EASYGUI::::::::::::::::::::::::::::::::::::::::::::::::::::::

#bekeres easyguival

benev=enterbox(msg="Kerek egy keresztnevet(0-val kilepes):")

#kiiras easyguival

msgbox(msg="",title="") #rovid szoveg kiirasa
textbox(msg="",title="", text="0") # text u.a mint a msg csak hozzabb szoveget lehet vele kiiratni(legordulo savval)
igen = buttonbox(msg="Kati ker meg lapot?",title=" 21-es játék",choices=("igen", "nem"))


#:::::::::::::::::::::::::::::::::::::::::::::::::::::file kezeles::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

# :::::::::::::::::::::::::::::::::::::::::::::::::::::TOMB::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# tomb random eleme
random.choice(tomb)


# int tomb novelese:
tomb.append(2)

#string tomb novelese:
tomb += "bele"

# eltuntetem az entereket az utolso szo vegerol
for i in range(7):
    p8[i] = p8[i][:-1]