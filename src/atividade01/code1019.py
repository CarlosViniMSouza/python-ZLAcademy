# -*- coding: utf-8 -*-

time = int(input())

hora = time // 3600
time %= 3600

min = time // 60
time %= 60

seg = time

print(f"{hora}:{min}:{seg}")