# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișează progresul inițial
print(" ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")

# Buclă principală de joc
while incercari_ramase > 0 and "_" in progres:
    # a. Cererea unei litere
    litera = input("Introdu o literă: ").lower()

    # b. Verificarea validității
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o literă validă.")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă.")
        continue

    # Adaugă litera în lista de litere încercate
    litere_incercate.append(litera)

    # c. Verificarea literei în cuvânt
    if litera in cuvant_de_ghicit:
        # Actualizează progresul
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Corect!")
    else:
        incercari_ramase -= 1
        print("Greșit! Încercări rămase:", incercari_ramase)

    # Afișarea progresului și încercărilor rămase
    print("Progres:", " ".join(progres))
    print("Încercări rămase:", incercari_ramase)

# Încheierea jocului
if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)
