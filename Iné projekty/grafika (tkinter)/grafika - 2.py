import tkinter, random
canvas = tkinter.Canvas(width=600,height=300)
canvas.pack()
x=random.randint(20,470)
y=random.randint(20,170)
xdl=10
ydl=10

for i in range(5):
    x=random.randint(20,600-20-xdl)
    y=random.randint(20,600-20-ydl)         #canvas = plátno
    canvas.create_line(x,y,x+xdl,+y+ydl)       #x - vždy prvá súradnica
    canvas.create_line(x+xdl,y+ydl,x+xdl,y)      #y - vždy druhá súradnica
    canvas.create_line(x+xdl,y,x,y)
    canvas.create_line(x,y,x,ydl+y)
    canvas.create_line(x,ydl+y,x+xdl,y)
    canvas.create_line(x,ydl+y,x+xdl,y+ydl)

