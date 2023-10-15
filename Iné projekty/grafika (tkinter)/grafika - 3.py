import tkinter, random
canvas = tkinter.Canvas(width=600,height=300)
canvas.pack()
x1=20
y1=20

for i in range(1000):
    x2=random.randint(20,600/2)
    y2=random.randint(20,300/2)
    canvas.create_line(x1,y1,x2,y2)

x1=580
y1=20    

for i in range(1000):
    x2=random.randint(600/2,580)
    y2=random.randint(20,300/2)
    canvas.create_line(x1,y1,x2,y2)

x1=580
y1=280

for i in range(1000):
    x2=random.randint(600/2,580)
    y2=random.randint(300/2,280)
    canvas.create_line(x1,y1,x2,y2)

x1=20
y1=280

for i in range(1000):
    x2=random.randint(20,600/2)
    y2=random.randint(300/2,280)
    canvas.create_line(x1,y1,x2,y2)
    
x1=20
y1=20    
