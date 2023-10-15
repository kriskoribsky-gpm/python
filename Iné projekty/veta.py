veta=input("Zadaj vetu")
novaveta=""
vpismeno=input("Zadaj veľké písmeno")
mpismeno=input("Zadaj malé písmeno")
dlzka=len(veta)
for i in range(dlzka):
    if veta[i]=="a":
        novaveta=novaveta+mpismeno
    elif veta[i]=="A":
        novaveta=novaveta+vpismeno
    else:
        novaveta=novaveta+veta[i]
print(novaveta)


#elif-shortcut for else if
#Tento program nahradí malé a veľké "a" písmenami, ktoré si zvolí užívateľ
