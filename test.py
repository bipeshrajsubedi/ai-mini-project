from tkinter import Tk, Frame, Button, Canvas, PhotoImage, NW, LEFT
from math import sqrt, hypot

from collections import namedtuple

# level - graph inp
k = 40
graph = {(500, 200): [(250, 300), (250, 1000)],
         (250, 300): [(250,1000),(500,500),(800,250)],
         (250, 1000): [(500,500),(800,1000)],
         (500,500):[(800,250),(800,1000)],
         (800,250) : [(800,1000),(1000,500)],
         (800,1000): [(1000,500)],
         (1000,500) : []

}

#check coordinates - event

def callback(event):
    print("",event.x,event.y)




#print(calculate_h(500, 200, 250, 300))
def draw():
    checkpoint = PhotoImage(file="checkpoint.png")
    for key, children in graph.items():
        x, y = key
        x_mid = ((2 * x + k) // 2)
        y_mid = ((2 * y + k) // 2)

        for x1, y1 in children:
            child_x_mid, child_y_mid = ((2 * x1 + k) // 2), ((2 * y1 + k) // 2)

            canv.create_line(x_mid, y_mid, child_x_mid, child_y_mid, width=30,fill="gray")
            canv.create_line(x_mid, y_mid, child_x_mid, child_y_mid, width=3, fill="white")
        canv.create_oval(x, y, x + k, y + k, fill="black")

        canv.create_image(x,y,image=checkpoint,anchor=NW)
        #print(checkpoint.type)





# calculate heuristics
def calculate_h(x1, y1, x2, y2):
    return hypot((x1 - x2), (y1 - y2))


ans = []
source = (500, 200)
destination = (1000, 500)

visited = dict()
cost_till = dict()
cost_till[source] = 0

def a_star(current, depth):
    if current == destination:
        return True

    x, y = current
    visited[current] = True

    minimum_f = float("inf")
    selected = None

    for child_x, child_y in graph[current]:
        g = cost_till[current] + calculate_h(child_x, child_y, x, y)
        h = calculate_h(child_x, child_y, destination[0], destination[1])
        f = g + h

        if f < minimum_f:
            minimum_f = f
            selected = (child_x, child_y)
            cost_till[selected] = cost_till[current] + calculate_h(child_x, child_y, x, y)

    if selected is not None:
        ans.append(selected)
        a_star(selected, depth + 1)


a_star(source, 0)


print(ans)


root = Tk()
root.geometry("1920x1080")
root.resizable(False,False)
canv = Canvas(root,width=1600, height=1600,bg="white")
canv.grid(row=0, column=0)
draw()


canv.bind("<Button-1>",callback)

root.mainloop()