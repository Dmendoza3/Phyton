from tkinter import Tk, Canvas, Frame, Button, BOTH

def hello(event):
    print("Single Click, Button-l") 

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Test")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 400, 400, outline="#fb0", fill="#fb0")
        canvas.pack(fill=BOTH, expand=1)

        canvas.bind('<Button-1>', hello)


def main():
    root = Tk()
    ex = Example()
    root.geometry("400x400+500+300")
    root.mainloop()
    
if __name__ == '__main__':
    main()