from tkinter import *
import random 
import time

class Ball:
    def __init__(self, can, color):
        self.canvas = can
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvasheight = self.canvas.winfo_height()
        self.canvaswidth = self.canvas.winfo_width()
        

    def draw(self):
        self.canvas.move(self.id, self.x, self.y )
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        elif pos[3] >= self.canvasheight:  # self.canvas.winfo_height():
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        elif pos[2] >= self.canvaswidth:  # self.canvas.winfo_width():
            self.x = -3
        


tk = Tk()
tk.title("Game")
tk.resizable(0, 0) # (False, False)
tk.wm_attributes("-topmost",1) # 1 = True
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()
ball = Ball(canvas, 'gold')
while 1:  
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.03)
tk.mainloop()