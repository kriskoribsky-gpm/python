import tkinter, random
canvas = tkinter.Canvas(width=400,height=400,bg="white")
canvas.pack()


def ciara(x,y,farba,cas):

    canvas.create_line(x,y,x,y+50, fill = farba, width = 30)
    
    canvas.update()             
    canvas.after(cas)           

              
    
for i in range(380,20,-5):

    ciara(i,200,"yellow",50)
    ciara(i,200,"white",50)
