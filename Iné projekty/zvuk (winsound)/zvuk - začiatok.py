import winsound, time
x=time.localtime()
winsound.Beep(500,250) #Hraj 250 milisekúnd na frekvencii 500 Hz
print("Hodín",str(x.tm_hour)+":"+str(x.tm_min))

