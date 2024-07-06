# -*- coding: utf-8 -*-

name = input()
salary = float(input())
totalSales = float(input())

totalCash = totalSales * 0.15 + salary

print(f"TOTAL = R$ %.2f" % totalCash)