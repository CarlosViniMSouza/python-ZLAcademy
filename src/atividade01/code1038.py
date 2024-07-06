# -*- coding: utf-8 -*-

req = input().split(' ')
cod = int(req[0])
quant = int(req[1])

match cod:
    case 1: 
        cash = quant * 4.00;
        print(f"Total: R$ {cash:.2f}")
    case 2: 
        cash = quant * 4.50;
        print(f"Total: R$ {cash:.2f}")
    case 3: 
        cash = quant * 5.00;
        print(f"Total: R$ {cash:.2f}")
    case 4: 
        cash = quant * 2.00;
        print(f"Total: R$ {cash:.2f}")
    case 5: 
        cash = quant * 1.50;
        print(f"Total: R$ {cash:.2f}")
