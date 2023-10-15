
#Tento program nahradí všetky samohlásky iným písmenom.
#or=alebo
#i-cyklus [i] pismenko v poradi cyklu


text1=("Sedi mucha na stene, na stene, na stene.")
text2=("Sedi mucha na stene, sedi a spi.")
text3=("Sedi a buvinka potvorka malinka.")
text4=("Sedi mucha na stene, sedi a spi.")

novytext1=(" ")
novytext2=(" ")
novytext3=(" ")
novytext4=(" ")

print("Nahradím  v texte <sedi mucha na stene> všetky samohlásky.")
zobrazit=input("Chceš zobraziť text pesničky ? (ano/nie)")
if zobrazit == "ano":
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    
pismeno=input("Akým písmenom chceš zameniť všetky samohlásky?")

for i in range(len(text1)):
    if  text1[i]=="a" or text1[i]=="e" or text1[i]=="i" or text1[i]=="o" or text1[i]=="u" or text1[i]=="ä" or text1[i]=="á" or text1[i]=="é" or text1[i]=="í" or text1[i]=="ó" or text1[i]=="ú":
        novytext1=novytext1+pismeno
       
    else:
        novytext1=novytext1+text1[i]


for i in range(len(text2)):
    if  text2[i]=="a" or text2[i]=="e" or text2[i]=="i" or text2[i]=="o" or text2[i]=="u" or text2[i]=="ä" or text2[i]=="á" or text2[i]=="é" or text2[i]=="í" or text2[i]=="ó" or text2[i]=="ú":
        novytext2=novytext2+pismeno
       
    else:
        novytext2=novytext2+text2[i]



for i in range(len(text3)):
    if  text3[i]=="a" or text3[i]=="e" or text3[i]=="i" or text3[i]=="o" or text3[i]=="u" or text3[i]=="ä" or text3[i]=="á" or text3[i]=="é" or text3[i]=="í" or text3[i]=="ó" or text3[i]=="ú":
        novytext3=novytext3+pismeno
       
    else:
        novytext3=novytext3+text3[i]


for i in range(len(text4)):
    if  text4[i]=="a" or text4[i]=="e" or text4[i]=="i" or text4[i]=="o" or text4[i]=="u" or text4[i]=="ä" or text4[i]=="á" or text4[i]=="é" or text4[i]=="í" or text4[i]=="ó" or text4[i]=="ú":
        novytext4=novytext4+pismeno
       
    else:
        novytext4=novytext4+text4[i]
        
        
print(novytext1)
print(novytext2)
print(novytext3)
print(novytext4)
