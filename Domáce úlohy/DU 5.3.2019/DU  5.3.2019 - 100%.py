x=input("Ako sa voláš ?")
y=int(input("Koľkokrát chceš zobraziť svoje meno ?"))

if y>20:
    print(y,"je veľa, stáčí ti napísať svoje meno 20krát.")
    y=20
    
for i in range(1,y+1):
    if y<21:
        print(str(i)+".",x)


    
    

    
