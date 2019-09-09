from tkinter import Tk, Canvas, Frame, Button, BOTH



class PaintFrame(Frame):
    def __init__(self):
        super().__init__()
        self.canvas = 0

        self.initUI()

        self.click = False
        self.pointList = []

        self.winX = 0
        self.winY = 0
        self.winW = 0
        self.winH = 0

    def setPosition(self, x = 0, y = 0):
        self.winX = x
        self.winY = y

    def setSize(self, w = 0, h = 0):
        self.winW = w
        self.winH = h

    def drawPoint(self):
        prevX, prevY = self.pointList[0]
        for x, y in self.pointList:
            self.canvas.create_line(prevX, prevY, x , y, fill="red")
            prevX, prevY = x,y
        self.pointList.clear()

    def click(self, event):
        self.click = True

    def unclick(self, event):
        self.click = False
        self.drawPoint()

    def mousemove(self, event):
        if self.click:
            self.pointList.append((event.x, event.y))

    def initUI(self):
        self.master.title("Test")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.create_rectangle(0, 0, 400, 400, outline="#fff", fill="#ddd")
        self.canvas.pack(fill=BOTH, expand=1)

        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<ButtonRelease-1>', self.unclick)
        self.canvas.bind('<Motion>', self.mousemove)


def main():
    root = Tk()
    ex = PaintFrame()
    ex.setPosition(500, 300)
    ex.setSize(300, 300)
    geometry = str(ex.winW) + "x" + str(ex.winH) + "+" + str(ex.winX) + "+" + str(ex.winY)
    root.geometry(geometry)
    root.mainloop()
    
if __name__ == '__main__':
    main()