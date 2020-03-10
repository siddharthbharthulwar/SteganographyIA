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
    def __init__(self, path, text):  
        self.img = cv.imread(path)
        self.b, self.g, self.r = cv.split(self.img)
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

    def moveBackCell(self):

        if (self.index > 0):
            self.index -= 1
        else:
            self.index = self.height - 1
            self.column -=1

    def encrypt(self, max):

        param = copy.deepcopy(self.b)
        green = copy.deepcopy(self.g)

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
            green[self.index, self.column] +=1
            self.moveCell()
        
        self.encrypted = param
        self.finalimage = cv.merge((self.r, self.g, param))

        plt.imshow(np.subtract(green, self.g))
        plt.show()
    
    def decrypt(self, max):

        self.index = 0
        self.column = 0
        param = np.abs(np.subtract(self.encrypted, self.b))

        plt.imshow(param)
        plt.show()
        max = 0
        maxFound = False
        valList = []
        #automatically detecting the max value from the encryption function
        while not maxFound:

            if (param[self.index, self.column] == 0):
                max +=1
                self.moveCell()
            else:
                maxFound = True
        while True:

            current = param[self.index, self.column]

            if (current == 0):

                self.moveCell()

                if (current == 0):

                    self.moveCell()

                    if (current == 0):

                        break
                    else:

            
                        self.moveBackCell()

            

im = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
file = open('data.txt', mode = 'r')
my = file.read()

eg = Encryption('clyde.jpg', my)
eg.encrypt(13)
plt.imshow(eg.finalimage)
plt.show()

#eg.decrypt(1)

    