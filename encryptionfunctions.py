import cv2 as cv 
import numpy
import matplotlib.pyplot as plt
import string
import numpy as np
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

def chooseMax(img, text):
    width = img.shape[1]
    height = img.shape[0]
    size = width * height
    mapped = map(text)
    sumZ = 0
    for i in range(len(mapped)):
        sumZ += mapped[i]
  #  return sumZ
    return int(size / sumZ)

def encrypt(img, text, max):
    param = copy.deepcopy(img)
    width = img.shape[1]
    height = img.shape[0]
    mapped = map(text)
    print(mapped)
    index = 0
    column = 0
    
    for i in range(max):
        if (index < height):
            index +=1
        else:
            index = 0
            column += 1
            index +=1
        

    for i in range(len(mapped)):
        val = mapped[i]

        div = truncate(val / max)


        for j in range(div):
            if (index < height):
                #print(index, column)
                param[index, column] +=1
                index +=1
            else:
                index = 0
                column +=1
                param[index, column] +=1
                index +=1

        if (index < height):
            param[index, column] += val - (truncate(val / max) * max)
            index +=1
        else:
            index = 0
            column +=1
            param[index, column] += val - (truncate(val / max) * max)
            index +=1
        
        if (index < height):
            param[index, column] = param[index, column]
            index +=1
        else:
            index = 0
            column +=1
            param[index, column] = param[index, column]
            index +=1
    return param

def move(array, index, column):
    height = array.shape[0]
    width = array.shape[1]

    if (index < height):
        index +=1
    else:
        index = 0
        column +=1



print(string.printable)
img = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
file = open('data.txt',mode='r')
my = file.read()
#my = "9abcdefgh"
plt.imshow(img)
plt.show()

encrypted = encrypt(img, my, 1)
plt.imshow(encrypted)
plt.show()

plt.imshow(img)
plt.show()
