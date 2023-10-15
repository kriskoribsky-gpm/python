
#Oprava znamok DU z informatiky

znamky="5,3,4,4,1,4,1"
noveznamky=""
dlzka=len(znamky)
for i in range(dlzka):
    if znamky[i]=="3" or znamky[i]=="4" or znamky[i]=="5":
        noveznamky=noveznamky + "1"
    else:
        noveznamky=noveznamky+znamky[i]
print(noveznamky)

