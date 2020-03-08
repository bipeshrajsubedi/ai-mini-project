from tkinter import Tk, Frame, Button, Canvas

class create_track:
    def __init__(self,frame,parent,childn):

        self.frame = frame
        self.parent = parent
        self.childn = childn




    def create_line(self):
        self.canvas = Canvas()
        #self.canvas.create_line(10,20,100,200,250,350,40,40)
        list = [(100, 100), (100, 200), (300, 300), (400, 300), (500, 100)]
        for x,y in list:
            print(x)
            print(y)
            self.canvas.create_oval(int(x),int(y),int(x)+50,int(y)+50)
            self.canvas.bind()
            self.canvas.pack()


    #frame = Frame(root, width=100, height=100)

    def create_graph(self):
        pass




def callback(event):
    print("clicked at",event.x, event.y)

def main():
    window = Tk()

    window.title("AI-GAME")
    window.geometry("1080x720")
    m_frame = Frame(window).pack()
    s_frame = Frame(window).pack(side='bottom')
    c_t = create_track(m_frame,None,None)
    c_t.create_line()
    m_frame.bind("<Button-1>", callback)
    m_frame.pack()
    window.mainloop()

if __name__ == '__main__':
    main()




