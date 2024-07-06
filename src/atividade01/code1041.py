# -*- coding: utf-8 -*-

points = input().split(' ')
X = float(points[0])
Y = float(points[1])

if(X > 0.0):
    if(Y > 0.0):
        print("Q1")
    elif(Y < 0.0):
        print("Q4")
    else:
        print("Eixo X")
elif(X < 0.0):
    if(Y > 0.0):
        print("Q2")
    elif(Y < 0.0):
        print("Q3")
    else:
        print("Eixo X")
else:
    if(Y > 0.0):
        print("Eixo Y")
    elif(Y < 0.0):
        print("Eixo Y")
    else:
        print("Origem")
