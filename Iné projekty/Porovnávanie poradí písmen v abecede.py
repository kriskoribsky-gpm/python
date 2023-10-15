
prve=input("Zadaj 1. meno")
meno=input("Zadaj 2. meno")

if prve > meno:
    prve=meno
#ak je prve meno abecedne za druhym, tak sa druhe premeni na prve 
meno=input("zadaj 3. meno")
if prve > meno:
        prve=meno

print("1. meno v abecede je",prve)
