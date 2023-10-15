
#tento program vypíše počet samohlások a z textu, ktorý zadá užívateľ

text=input("Zadaj text:")
a=0
for i in range(len(text)):
    if text[i]=="a":
        a=a+1


print("Počet samohlások a v texte=",a)
