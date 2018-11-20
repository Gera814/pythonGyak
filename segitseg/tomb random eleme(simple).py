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


lista = ["zsuzsi", "peti", "pali", "zita", "inez"]

print sample(lista,1) # a lista 1db random elemet adja vissza

#kiiratas fileba
file = open("out.txt", "w")
file.write(sample(lista,1)[0]) # a simple tombosit, ezert le kell szedni []-ket, hogy szep legyen a kiiratas
                                # ha meg egy [0]-t irok akkor csak a nev elso betujet irja ki.
file.close()