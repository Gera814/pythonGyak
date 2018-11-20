#!/usr/bin/pyton
# -*- coding: utf-8 -*-

lista = [5, -3, 9, -1, 7]
nevek = ["Berta Andrea", "Aladics Geza", "Certics Zita"]

print (sorted(lista, key=abs, reverse=False)) # reverse= False -> növekvő lista

print (sorted(nevek, reverse= True)) # nevek rendezese


# rendezes keresztnev szerint fny-el
def keresztnev_elso_betuje(nev):
    return nev.split()[1][0]     # [1] --> nézi [[Berta], [Andrea]] 1. indexét és [0] --> nézi [Andrea] 0. indexét ->> Andrea (magyarul [0] lebontja a []-t) 

print(sorted(nevek, key=keresztnev_elso_betuje)) 

#rendezés for-al
 
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i] > lista [j]:
            lista[i], lista[j] = lista[j], lista[i]
            
print "rendezes for-al", lista      