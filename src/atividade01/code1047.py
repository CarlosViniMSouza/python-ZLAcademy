# -*- coding: utf-8 -*-

[Hi, Mi, Hf, Mf] = [
    int(x) for x in input().strip().split(' ')
]

init = Hi * 60 + Mi
final = Hf * 60 + Mf

if final <= init:
    final += 24 * 60

print(f"O JOGO DUROU {(final - init) // 60} HORA(S) E {(final - init) % 60} MINUTO(S)")