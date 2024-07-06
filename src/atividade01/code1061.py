# -*- coding: utf-8 -*-

def convertTime(day, hour, min, seg):
    return (24 * 60 * 60) * day + (60 * 60) * hour + 60 * min + seg

Di = int(input().split(' ')[1])
Hi, Mi, Si = [int(x) for x in input().split(' : ')]

Df = int(input().split(' ')[1])
Hf, Mf, Sf = [int(x) for x in input().split(' : ')]

init = convertTime(Di, Hi, Mi, Si)
final = convertTime(Df, Hf, Mf, Sf)

gap = final - init

print(f'{gap//(24 * 60 * 60)} dia(s)')
gap %= (24 * 60 * 60)

print(f'{gap//(60 * 60)} hora(s)')
gap %= (60 * 60)

print(f'{gap//60} minuto(s)')
gap %= 60

print(f'{gap} segundo(s)')