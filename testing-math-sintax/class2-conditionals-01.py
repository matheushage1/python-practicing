# Conditionals: if, else, elif

numero_de_atrasos = 0

if numero_de_atrasos >= 3:
    print("Você está suspenso.")
elif numero_de_atrasos == 2:
    print("Você já possui duas faltas. Cuidado.")
elif numero_de_atrasos == 1:
    print("Você possui uma falta, o máximo são três.")
else:
    print("Você está liberado. 0 faltas.")