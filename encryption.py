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
        else:
            self.index = 0
            self.column +=1

    def encrypt(self, max):

        param = copy.deepcopy(self.img)

        for i in range(max):
            self.moveCell()
        
        for i in range(len(self.mapped)):

            val = self.mapped[i]
            div = truncate(val / max)

            for j in range(div):
                
                if (param[self.index, self.column] > 120):
                    param[self.index, self.column] -=1
                else:
                    param[self.index, self.column] += 1


                param[self.index, self.column] +=1
                self.moveCell()

            if (param[self.index, self.column] > 120):
                param[self.index, self.column] -= val - (truncate(val / max) * max)

            else:
                param[self.index, self.column] += val - (truncate(val / max) * max)

            self.moveCell()
            self.moveCell()
        
        self.encrypted = param
    
    def decrypt(self, max):

        self.index = 0
        self.column = 0
        param = np.abs(np.subtract(self.encrypted, self.img))
        max = 0
        maxFound = False
        while not maxFound:

            if (param[self.index, self.column] == 0):
                max +=1
                self.moveCell()
            else:
                maxFound = True
        print(max)


im = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
file = open('data.txt', mode = 'r')
my = file.read()

eg = Encryption(im, my)
eg.encrypt(13)
plt.imshow(eg.encrypted)
plt.show()

eg.decrypt(1)

    