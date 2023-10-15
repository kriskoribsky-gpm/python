import random
slovnik=["slovo","veta","text"]
pocet=len(slovnik)
vyber=random.randint(0,pocet)


slovo=slovnik[vyber]
tajne=len(slovo)*"x"
print(tajne)
cislo=""
for i in range(1,len(slovo)+1):
    cislo=cislo+str(i)
print(cislo)
zobraz=""
hadaj=""
while hadaj != slovo:                      #!= je nerovná sa
    z=int(input("Zadaj císlo"))-1
    for i in range(len(slovo)):
        if i==z:
            zobraz=zobraz+slovo[i]
        else:
            zobraz=zobraz+tajne[i]
    print(zobraz)
    hadaj=input("Hádaj slovo:")
    if hadaj == slovo:
        print("Neuhádol si!")
print("Uhádol si!")
