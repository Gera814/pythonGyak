#!usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import string
from easygui import *
import easygui
import math

'''
Feladat:

1. Készítsen egy programot, amely addig olvas be vidám (mosolygós, nevetős, pl. :), :-), :D stb.)
smiley-kat egy listába, amíg a felhasználó nem visz be üres stringet (üres Enter). Ezután kérjen egy
másik listába negatív (szomorú, mérges stb.) arcokat. Végül írja ki a megismert smiley-kat a képernyőre!
'''

vidam = []
szomoru = []
besmiley = ""
for i in range(100):
    besmiley = raw_input("Kerek egy nevetos smiley-t:")
    if besmiley == "":
        break
    else:
        vidam.append(besmiley)
        besmiley = ""

for i in range(100):
    besmiley = raw_input("Kerek egy szomoru smiley-t:")
    if besmiley == "":
        break
    else:
        szomoru.append(besmiley)
        besmiley = ""

print "vidamak"

for i in range(len(vidam)):
    print vidam[i]
       
print "szomoruak:"       
for i in range(len(szomoru)):
    print szomoru[i]

file = open("vidam.txt","a")
for i in range(len(vidam)):
    file.write(vidam[i] + ", ")
        
file.close()

file = open("szomoru.txt", "a")
for i in range(len(vidam)):
    file.write(szomoru[i] + ", ")
file.close()