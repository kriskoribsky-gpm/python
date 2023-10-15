
def rainScene(drop_lenght,scene_height,scene_width):
    import random, tkinter
    x = random.randint(1,1200)
    y = random.randint(1,600)
    x1 = x - drop_lenght
    y1 = y - drop_lenght
    rainScene = tkinter.Canvas(width = scene_width, height = scene_height)
    rainScene.pack()
    rainScene.create_line(x,y,x1,y1)
    
    
def city(house_width,house_height,house_count,street_width,street_height):
    import random, tkinter
    def dom(a,b,c):
        x = random.randint(1,1200)
        y = random.randint(1,600)
        x1 = x - a
        y1 = y - b
        house = tkinter.Canvas(width = house_width, height = house_height)
        house.pack()
        for i in range(c):
            house.create_rectangle(x,y,x1,y1)
        def ulica(a,b)
        






            
        dom(house_width,house_height,house_count)
        

        
    


    
