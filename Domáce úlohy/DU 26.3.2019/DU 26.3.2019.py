
#tento program,v ktorom užívateľ napíše meno a priezvisko oddelene
#vypíše len priezvisko: -priezvisko-

meno=input("Zadaj meno a priezvisko:")
priezvisko=1
for i in range(len(meno)):
    if meno[i]==" ":
        priezvisko=priezvisko+i
        
print("-"+str((meno[priezvisko:len(meno)]))+"-")
