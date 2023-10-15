import tkinter
canvas = tkinter.Canvas(width=600,height=300)
canvas.pack()                           #canvas = plátno
canvas.create_line(20,20,580,280)       #x - vždy prvá súradnica
canvas.create_line(580,280,580,20)      #y - vždy druhá súradnica
canvas.create_line(580,20,20,20)
canvas.create_line(20,20,20,280)
canvas.create_line(20,280,580,20)
canvas.create_line(20,280,580,280)
