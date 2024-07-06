# -*- coding: utf-8 -*-

cod = int(input())

match cod:
    case 11:
        print("Sao Paulo")
    case 19:
        print("Campinas")
    case 21:
        print("Rio de Janeiro")
    case 27:
        print("Vitoria")
    case 31:
        print("Belo Horizonte")
    case 32:
        print("Juiz de Fora")
    case 61:
        print("Brasilia")
    case 71:
        print("Salvador")
    case _:
        print("DDD nao cadastrado")
