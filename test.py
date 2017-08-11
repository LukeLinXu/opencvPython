# import numpy as np
import cv2
from PIL import ImageTk
import PIL.Image
from tkinter import *


def sel(var1):
   var1 = '20'
   im = cv2.imread('2.jpg')
   im = cv2.GaussianBlur(im, (3, 3), 0)
   canny = cv2.Canny(im, int(var1), int(var1)*3)
   ret, thresh = cv2.threshold(canny, 127, 255, 0)
   im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   area = -1
   cnt = contours[0]
   for cnt0 in contours:
       t = cv2.contourArea(cnt0)
       if t > area:
           cnt = cnt0
           area = t

   # epsilon = 0.1 * cv2.arcLength(cnt, True)
   # approx = cv2.approxPolyDP(cnt, epsilon, True)
   # cv2.drawContours(im, [approx], -1, (0, 255, 0), 3)

   cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
   cv2.imwrite(path, im2)
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

