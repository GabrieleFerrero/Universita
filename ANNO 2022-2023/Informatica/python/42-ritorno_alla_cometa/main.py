"""
Una persona mediamente può saltare staccandosi da terra con una
velocità di 11 chilometri orari senza dover temere di lasciare la superficie terrestre. Al contrario, se
una persona saltasse con la stessa velocità mentre si trova sulla Cometa di Halley, riuscirebbe a
tornare sulla superficie? Creare un programma che permetta all’utente di inserire in input una
velocità di lancio (in km orari) dalla superficie della Cometa di Halley, e di determinare se la persona
che salta sarà in grado di tornare sulla superficie. In caso contrario, il programma dovrà calcolare
quanta massa in più dovrebbe avere la cometa perché accada.
Suggerimento: la velocità di fuga è
𝜐𝑒𝑠𝑐𝑎𝑝𝑒 = √2 𝐺 𝑀
𝑅 ,
dove 𝐺 = 6.67 × 10 −11 𝑁 𝑚2 / 𝑘𝑔2 è la costante gravitazionale, 𝑀 è la massa del corpo celeste,
ed 𝑅 è il suo raggio. La Cometa di Halley ha una massa di 2.2 × 1014 𝑘𝑔 ed un diametro di 9.4 𝑘𝑚 .
"""


G = 6.67*10e-11
M = 2.2*10e14
R = 9400/2

import math

velocita = float(input("Inserire la velocità: "))*1000/3600

if velocita > math.sqrt(2*((G*M)/R)):
    print(f"A questa velocità non ritorneresti sulla superficie, ma se la massa della cometa fosse di {((velocita**2)*R)/(G*2)}kg invece rimarresti")
else: print("A questa velocità rimarresti sulla superficie")