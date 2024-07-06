salary = float(input())
upSalary = 0

if salary <= 400.00:
    upSalary = 15
elif salary <= 800.00:
    upSalary = 12
elif salary <= 1200.00:
    upSalary = 10
elif salary <= 2000.00:
    upSalary = 7
else:
    upSalary = 4

newSalary = salary * (1 + upSalary / 100)
upSalaryWon = salary * upSalary / 100

print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {upSalaryWon:.2f}')
print(f'Em percentual: {upSalary} %')