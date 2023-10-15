import drop, tkinter

drop.drop(20)
rainScene = tkinter.Canvas(width = 1200, height = 600)
rainScene.pack()
for i in range(1000):
    rainScene.create_line(x, y, x1, y1)
