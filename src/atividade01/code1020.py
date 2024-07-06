# -*- coding: utf-8 -*-

days = int(input())

years = days // 365
days %= 365

mounths = days // 30
days %= 30

print(f"{years} ano(s)")
print(f"{mounths} mes(es)")
print(f"{days} dia(s)")