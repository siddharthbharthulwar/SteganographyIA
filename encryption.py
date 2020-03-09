import numpy as np 
import matplotlib.pyplot as plt 
import cv2 as cv
import string 
import copy

def truncate(num):
    text = str(num)
    pointIndex = text.index('.')
    newText = ""
    for i in range(pointIndex):
        newText += text[i]
    return int(newText)

def map(text):
    charList = string.printable
    intList = []
    for i in range(len(text)):
        intList.append(charList.index(text[i]) + 1)
    return intList



class Encryption:  
    
    # init method or constructor   
    def __init__(self, image, text):  
        self.img = image
        self.txt = text
        self.mapped = map(self.txt)
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]
        self.index = 0
        self.column = 0
    
    def moveCell(self):

        if (self.index < self.height - 1):
            self.index +=1
          #  print(self.index, "/", self.height)
        else:
            self.index = 0
            self.column +=1
            print("condition two")

    def encrypt(self, max):

        param = copy.deepcopy(self.img)

        for i in range(max):
            self.moveCell()
        
        for i in range(len(self.mapped)):

            val = self.mapped[i]
            div = truncate(val / max)

            for j in range(div):
                param[self.index, self.column] +=1
                self.moveCell()

            param[self.index, self.column] += val - (truncate(val / max) * max)
            self.moveCell()
            self.moveCell()
        
        return param
    


im = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
file = open('data.txt', mode = 'r')
my = file.read()

eg = Encryption(im, my)
plt.imshow(eg.encrypt(1))
plt.show()


    