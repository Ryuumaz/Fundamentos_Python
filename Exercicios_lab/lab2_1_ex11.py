'''
11. Desenvolva um programa a solicitar a entrada de horas, minutos e segundos, calculando depois o tempo
    total em segundos.
'''
print("\nExercício 11\n")

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_em_segundos = horas * 3600 + minutos * 60 + segundos
print("Total em segundos: %ds." % total_em_segundos)