x=(input("Ako sa voláš ?"))
y=int(input("Koľkokrát chceš vypísať tvoje meno ?"))
for i in range(1,y+1):
    if y<21:
        print(str(i)+".",x)
        
if y>20:
    print(y, "je veľa. Maximálny počet zobrazenia tvojho mena je 20krát.")    


