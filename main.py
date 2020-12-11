from tkinter import *
import numpy as np
import math
import copy

master = Tk()

w = Canvas(master, width=800, height=800)
w.configure(scrollregion=(-400,-400, 400, 400))
w.xview_moveto(.5)
w.yview_moveto(.5)
w.pack()

ogview = np.transpose(np.matrix([[-200,-200,-200],[-200,-200,200],[200,-200,200],[200,-200,-200],[-200,200,-200],[-200,200,200],[200,200,200],[200,200,-200]]))
view = copy.deepcopy(ogview)
links = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]

FOV = math.radians(90)
fCoe = 1 / math.tan(FOV / 2)
print(fCoe)
def draw():
    for link in links:
        global view
        viewt = np.transpose(view)
        w.create_line(fCoe * viewt[link[0],0],fCoe * viewt[link[0],1], fCoe *viewt[link[1],0],fCoe * viewt[link[1],1], fill="#476042", width=3)

def rotZ(theta):
    rotMat = np.transpose(np.matrix([[1,0,0],[0,math.cos(theta),math.sin(theta)],[0,-math.sin(theta),math.cos(theta)]]))
    global view
    view = rotMat * view

def rotY(theta):
    rotMat = np.matrix([[math.cos(theta),0,math.sin(theta)],[0,1,0],[-math.sin(theta),0,math.cos(theta)]])
    global view
    view = rotMat * view

def rotX(theta):
    rotMat = np.matrix([[1,0,0],[0,math.cos(theta),-math.sin(theta)],[0,math.sin(theta),math.cos(theta)]])
    global view
    view = rotMat * view

while 1:
    draw()
    rotY(0.01)
    rotZ(0.01)
    rotX(0.01)
    w.update()
    w.after(10)
    w.delete("all")

mainloop()