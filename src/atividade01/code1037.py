# -*- coding: utf-8 -*-

quant = float(input())

if 0 <= quant <= 25:
    print("Intervalo [0,25]")
elif 25 < quant <= 50:
    print("Intervalo (25,50]")
elif(50 < quant <= 75):
    print("Intervalo (50,75]")
elif 50 < quant <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")