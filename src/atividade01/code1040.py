# -*- coding: utf-8 -*-

notes = input().strip().split(' ')

note1 = float(notes[0])
note2 = float(notes[1])
note3 = float(notes[2])
note4 = float(notes[3])

mean = (note1*2 + note2*3 + note3*4 + note4*1) / 10

print(f"Media: {mean:.1f}")

if mean < 5.0:
    print("Aluno reprovado.")
elif mean >= 7.0:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    
    test = float(input().strip())
    print(f"Nota do exame: {test:.1f}")

    mean = (mean + test) / 2

    if(mean >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {mean:.1f}")