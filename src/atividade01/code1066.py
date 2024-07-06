# -*- coding: utf-8 -*-

odd, posi, nega = 0, 0, 0
for _ in range(5):
    num = int(input())

    if abs(num) % 2:
        odd += 1
    if num > 0:
        posi += 1
    elif num < 0:
        nega += 1

print(f'{5 - odd} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{posi} valor(es) positivo(s)')
print(f'{nega} valor(es) negativo(s)')