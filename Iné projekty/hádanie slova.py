import random

slovo="gymnázium"
tajne=len(slovo)*"*"
cislo=""
zobraz=""
X=0

hadaj=""
for y in range(1,len(slovo)+1):
    cislo=cislo+str(y)
print(cislo)
print(tajne)
while hadaj != slovo or zobraz != slovo:     #!= znamená, že sa nerovná
    x=int(input("Písmeno v akom poradí chceš odkryť? (napíš císlicou):"))-1
    print(cislo)
    for z in range(len(slovo)):
        if x==z:
           zobraz=zobraz+slovo[z]
        else:
            
    print(zobraz)
    print(tajne)
    print(cislo)
    
    
    
        
    
    


