import tkinter, random
canvas = tkinter.Canvas(width = 400, height = 400, bg = "white") #bg = background color
canvas.pack()

i = 0

def kruh(x,y,r,farba,cas):

    canvas.create_oval(x-r,y-r,x+r,y+r, outline = "white", fill = farba)
    canvas.update()             
    canvas.after(cas)           

              #canvas.update() = zobrazí dosial nakreslené veci
              #canvas.after = spomalenie programu o x milisekúnd
              #outline = farba obvodu

x = 20
y = 20

for i in range(500):

    kruh(x,y,r,"#f9460b",20)     #červená farba zo skicáru v hexadecimálnej sústavy
    
    x = x + random.randint(-10,10)
    y = y + random.randint(-10,10)
    r = 10
    
    if x < 380:
        x = 380
    if x < 0:
        x = 0
    if x < -380:
        x = -380

    if y < 380:
        y = 380
    if y < -380:
        y = -380
    if y < 0:
        y = 0





