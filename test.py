# import numpy as np
import cv2
from PIL import ImageTk
import PIL.Image
from tkinter import *


def sel(var1):
   im = cv2.imread('3.jpg')
   im = cv2.GaussianBlur(im, (3, 3), 0)
   canny = cv2.Canny(im, int(var1), int(var1)*3)
   # output1 = []
   # output2 = []
   # cv2.findContours(canny, output1, output2, )
   cv2.imwrite(path, canny)
   img2 = ImageTk.PhotoImage(PIL.Image.open(path))
   panel.configure(image=img2)
   panel.image = img2

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var, command=sel)
scale.pack(anchor=CENTER, side = "left")

path = 'canny.jpg'

img = ImageTk.PhotoImage(PIL.Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "right", fill = "both", expand = "yes")
root.mainloop()

