# coding:utf-8

# huszonegyes

'''
Python2 pĂłt-zĂĄrthelyi feladatsor â 2017. december 11.

Ărjon programot, ami megvalĂłsĂ­tja a "Huszonegyes" jĂĄtĂŠkot.
(Info: https://hu.wikipedia.org/wiki/Huszonegyes)

1. feladat (10 pont)
Hozzon lĂŠtre kĂŠt listĂĄt, amely a jĂĄtĂŠkhoz szĂźksĂŠges adatokat (lapokat ĂŠs ĂŠrtĂŠkeket) tĂĄrolja.
EzutĂĄn Ă­rassa ki az Ăśsszes lapot ĂŠs zĂĄrĂłjelben az ĂŠrtĂŠkĂŠt az alĂĄbbi formĂĄban:
VII (7), VIII (8), IX (9), X (10), AlsĂł (2), FelsĹ (3), KirĂĄly (4), Ăsz (11)
'''

import random as r

def pontokOsszegzese(jatekosIndexe):
	jatekosPontszama = 0
	# Ă­gy nĂŠz ki a kĂŠt lista, ezekbĹl kĂŠne kibogarĂĄszni az ĂśsszpontszĂĄmot:
	# jatekosokLapok = [ [ "Kati", [0,7]], ["Zsuzsi", [4,2]], ... ]
	# lapok = [["VII",7], ["VIII",8], ["IX",9], ["X",10], ["Also",2], ["Felso",3], ["Kiraly",4], ["Asz",11] ]
	print
	# print ">>>%s lapindexei: %s: " % (jatekosokLapok[jatekosIndexe][0], str(jatekosokLapok[jatekosIndexe][1]) )
	for aktualLapIndex in range(len(jatekosokLapok[jatekosIndexe][1])): # ahĂĄny lapja van, azon mind vĂŠgigmegyĂźnk
		aktualLap = jatekosokLapok[jatekosIndexe][1][aktualLapIndex]
		# print "...>>> aktualis lap indexe: ", aktualLap # TESZTELĂSHEZ
		aktualPont = lapok[aktualLap][1]
		# print "......>>> aktualis pontszam: ", aktualPont # TESZTELĂSHEZ
		
		jatekosPontszama += aktualPont
	return jatekosPontszama

def kiirJatekAllasa():
	print
	for jat in range(len(jatekosokLapok)): # sorra vesszĂźk az Ăśsszes jĂĄtĂŠkost
		aktualJatekosLapjai = "" # ebbe a sztringbe fogjuk tenni a kiĂ­rnivalĂł lapokat
		aktualisPontszamokOsszege = 0
		for lap in range(len(jatekosokLapok[jat][1])): # az adott jĂĄtĂŠkos minden lapja
			# print jatekosokLapok[jat][1][lap], # itt sorolja fel az indexeket
			aktualLapIndexe = jatekosokLapok[jat][1][lap]
			aktualJatekosLapjai += lapok[aktualLapIndexe][0]
			if lap+1 < len(jatekosokLapok[jat][1]): # ha nem az utolsĂł lap, akkor vesszĹ is kell
				aktualJatekosLapjai += ", "
			aktualisPontszamok = lapok[aktualLapIndexe][1]
			aktualisPontszamokOsszege += aktualisPontszamok
			# print aktualisPontszamok, "-",	 # TESZTELĂSHEZ
		print "%s:\t" % jatekosokLapok[jat][0], # az adott jĂĄtĂŠkos neve
		print "%4d\t%s" % (aktualisPontszamokOsszege, aktualJatekosLapjai)
		#print ">>> PONT: ", pontokOsszegzese(jat)  # TESZTELĂSHEZ

print "21-ezzunk!"

# az elsĹ feladat kĂŠt listĂĄt kĂŠr, de mivel kĂŠsĹbb jogom van ĂĄtĂ­rni, ha mĂĄshogy praktikusabbnak tĹąnik,
# a vĂŠgsĹ megoldĂĄsban egy Ăśsszetett listĂĄt hasznĂĄlok

lapok = [["VII",7], ["VIII",8], ["IX",9], ["X",10], ["Also",2], ["Felso",3], ["Kiraly",4], ["Asz",11] ]
kiir = "" # ebbe a stringbe gyĹąjtĂśm Ăśssze a kiĂ­rnivalĂłt
for i in range(len(lapok)):
	# print lapok[i ][0], "(", lapok[i][1], ")", 
	# majdnem jĂł, de Ă­gy sajnos beletesz a zĂĄrĂłjelen belĂźl egy-egy szĂłkĂśzt,	
	# ezĂŠrt kerĂźlĹ megoldĂĄskĂŠnt elĹbb felĂŠpĂ­tek egy sztringet, ĂŠs azt Ă­rom ki:
	kiir += lapok[i][0] + " (" + str(lapok[i][1]) + ")"
	if lapok[i][0] != 'Asz':
		kiir += ", "
print "\n", kiir


'''
2. feladat (20 pont)
A program adjon kĂŠt-kĂŠt vĂŠletlen lapot mind a nĂŠgy jĂĄtĂŠkosnak (Kati, Zsuzsi, Peti, Pali).
Ărja ki az alĂĄbbi formĂĄban (a pontszĂĄmokat helyiĂŠrtĂŠk szerint igazĂ­tva) a jĂĄtĂŠkosok pillanatnyi ĂĄllĂĄsĂĄt:
Kati:	6	AlsĂł, KirĂĄly
Zsuzsi:	18	VII, Ăsz
Peti:	17	IX, VIII
Pali:	10	FelsĹ, VII
'''

# Szebb, ha ĂĄltalĂĄnos szĂĄmĂş felhasznĂĄlĂłra mĹąkĂśdik.
# ElfogadhatĂł az is, ha csak 4-re Ă­rjuk meg, tehĂĄt pl. van 4 pontszĂĄm-vĂĄltozĂł stb.

jatekosokLapok = []
# terv: [ [ nĂŠv_1, [lapok_indexei_1] ], [ nĂŠv_2, [lapok_indexei_2] ], ...]
# pl:     [ [ "Kati", [0,7]], ["Zsuzsi", [4,2]]]
# vagyis Kati lapjai: VII, Asz, Zsuzsi lapjai: Also, VIII

# az ĂśsszpontszĂĄmot nem kell tĂĄrolni, majd mindig kiszĂĄmolom
# vĂŠletlen szĂĄmokat generĂĄlunk, 0 ĂŠs 7 kĂśzĂśtt, ĂŠs ezzel megvan a lap indexe (0: VII, 7: Asz)

jatekosokLapok.append(["Kati"])
jatekosokLapok.append(["Zsuzsi"])
jatekosokLapok.append(["Peti"])
jatekosokLapok.append(["Pali"])
# jatekosokLapok.append(["POTYAUTAS"])
# tĂśbb jĂĄtĂŠkosnĂĄl tovĂĄbb bĹvĂ­thetĹ a lista
#print jatekosokLapok  # TESZTELĂSHEZ

# kapnak kĂŠt kezdĹ lapot
for jat in range(len(jatekosokLapok)):
	jatekosokLapok[jat].append([])
	for j in range(2):
		jatekosokLapok[jat][1].append(r.randint(0,7))

# emlĂŠkeztetĹ: ilyen legyen a kiĂ­rĂĄs:
# Kati:	6	AlsĂł, KirĂĄly

kiirJatekAllasa()


'''
3. feladat (20 pont)
BĹvĂ­tse a feladatot, kĂŠrdezze meg a program minden egyes jĂĄtĂŠkostĂłl sorban (ĂŠs aztĂĄn majd tovĂĄbbi kĂśrĂśk-ben), hogy kĂŠr-e mĂŠg lapot. Aki kĂŠr, annak adjon egy-egy vĂŠletlen lapot. (VĂŠgtelen szĂĄmĂş paklival dolgo-zunk, a lapok nem fogynak el.) Minden egyes kĂśr utĂĄn Ă­rja ki a jĂĄtĂŠk ĂĄllĂĄsĂĄt, mint a 2. lĂŠpĂŠsben.
'''

kerMegLapot = [] # ebben tĂĄroljuk, hogy ki kĂŠr mĂŠg lapot
for i in range(len(jatekosokLapok)):
	kerMegLapot.append(1)
hanyanKernekMeg = len(jatekosokLapok)

while hanyanKernekMeg > 0:
	print
	for jat in range(len(jatekosokLapok)):
		if kerMegLapot[jat] == 1:
			kerLapot = raw_input( jatekosokLapok[jat][0] + ", kersz lapot? (I/N) ")
			if kerLapot.upper() == 'I': 	# upper(), hogy elfogadjon kisbetĹąt is (ĂŠs illene hibakezelĂŠs...)
				jatekosokLapok[jat][1].append(r.randint(0,7))
			else:
				kerMegLapot[jat] = 0
				hanyanKernekMeg -= 1
		else:
			print jatekosokLapok[jat][0], "\t--- (Mar az elobb sem kert.)"
	kiirJatekAllasa()

'''
4. feladat (10 pont)
Hirdesse ki a program, hogy ki esett ki (akinek 21-nĂŠl tĂśbb pontja van), illetve ki nyerte a jĂĄtĂŠkot (akinek legtĂśbb, de 22-nĂŠl kevesebb pontja van). (A valĂłs jĂĄtĂŠkban a kĂŠt ĂĄsz ĂŠrtĂŠkesebb, mint az ĂŠppen 21 pont, plusz pontĂŠrt ezt is beleveheti az ĂŠrtĂŠkelĂŠsbe.)
'''

versenybenVannak = []

for jat in range(len(jatekosokLapok)):
	jatekosOsszpontszama = pontokOsszegzese(jat)
	if jatekosOsszpontszama > 21:
		print jatekosokLapok[jat][0], jatekosOsszpontszama, " ponttal kiesett."
	else:
		print "%s versenyben van %d ponttal." % (jatekosokLapok[jat][0], jatekosOsszpontszama)
		versenybenVannak.append([jatekosokLapok[jat][0], jatekosOsszpontszama])
#print "Versenyben vannak:", versenybenVannak	 # TESZTELĂSHEZ

# A holtverseny miatt szĂĄmlĂĄljuk, hogy hĂĄny nyertes van ĂŠppen
nyertesekSzama = 0
nyertesek = ""
# Akik nem estek ki: [nĂŠv, pontszĂĄm]

if len(versenybenVannak) > 0:
	gyoztesPont = 0
	for i in range(len(versenybenVannak)):
		# print "versenybenVannak:", versenybenVannak				 # TESZTELĂSHEZ
		# print "versenybenVannak[i]:", versenybenVannak[i]			 # TESZTELĂSHEZ
		# print "versenybenVannak[i][0]:", versenybenVannak[i][0]	 # TESZTELĂSHEZ
		
		if versenybenVannak[i][1] > gyoztesPont:
			gyoztesPont = versenybenVannak[i][1]
			nyertesekSzama = 1
			nyertesek = ""
			nyertesek += versenybenVannak[i][0]
			nyer = "nyertes" # egyes szĂĄm
		elif versenybenVannak[i][1] == gyoztesPont:
			nyertesekSzama += 1
			if nyertesekSzama > 0: # mĂĄr van valaki a listĂĄn
				nyertesek += ", "
			nyertesek += versenybenVannak[i][0]
			nyer = "nyertesek" # tĂśbbes szĂĄm
	
	print "Nyertesek szama: %d, gyoztes pontszam: %d, %s: %s" % (nyertesekSzama, gyoztesPont, nyer, nyertesek)
else:
	print "Nincs gyoztes, mindenki kiesett."

'''
5. extra feladat (20 pont)
Tartsa szĂĄmon a program, hogy 32 lapja van a magyar kĂĄrtyĂĄnak, ĂŠs pl. ha nĂŠgy kirĂĄly mĂĄr kĂŠzben van, akkor ne adjon ĂśtĂśdiket.
'''

# coming soon...