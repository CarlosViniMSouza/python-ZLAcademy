values = input().split(' ')
code1 = int(values[0])
quant1 = int(values[1])
value1 = float(values[2])

values = input().split(' ')
code2 = int(values[0])
quant2 = int(values[1])
value2 = float(values[2])

total = (quant1 * value1 + quant2 * value2)

print(f"VALOR A PAGAR: R$ {total:.2f}")