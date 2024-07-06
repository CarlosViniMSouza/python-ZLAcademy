# -*- coding: utf-8 -*-

quant = int(input())

print(quant)

print(f"{quant // 100} nota(s) de R$ 100,00")
quant %= 100

print(f"{quant // 50} nota(s) de R$ 50,00")
quant %= 50

print(f"{quant // 20} nota(s) de R$ 20,00")
quant %= 20

print(f"{quant // 10} nota(s) de R$ 10,00")
quant %= 10

print(f"{quant // 5} nota(s) de R$ 5,00")
quant %= 5

print(f"{quant // 2} nota(s) de R$ 2,00")
quant %= 2

print(f"{quant} nota(s) de R$ 1,00")