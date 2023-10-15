
#Tento program výpíše na plátne iniciálky K.K

import tkinter
canvas = tkinter.Canvas(width=1200, height=900) #vytvorí plátno (canvas)
canvas.pack()                                   #s rozmermi 1200 (šírka)
x = 300         #x = vždy sírková súradnica     #a 900 (výška)
y = 200         #y = vždy výšková súradnica
p = 450


canvas.create_line(x,y,x,700, width = 10, fill = "green")
canvas.create_line(x,p,500,y, width = 10, fill = "green")
canvas.create_line(x,p,500,y+500, width = 10, fill = "green")

x = 700
y = 200

canvas.create_line(x,y,x,x, width = 10, fill = "green")
canvas.create_line(x,p,900,y, width = 10, fill = "green")
canvas.create_line(x,p,900,y+500, width = 10, fill = "green")

