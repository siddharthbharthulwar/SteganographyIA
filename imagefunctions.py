import cv2 as cv 
import numpy
import matplotlib.pyplot as plt
import string
import numpy as np

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


def encrypt(image, text, max):
    
    new = image
    mapped = map(text)
    width = image.shape[0]
    height = image.shape[1]
    print(width, height)
    column = 0
    index = 0
    for i in range(len(mapped)):
        print(i)
        val = mapped[i]
        div = truncate(val / max)


        for j in range(div):
            if (index < height):
                new[index, column] += -1
                index +=1
            else:
                column +=1
                index = 0
                new[index, column] += -1
                index +=1
        

        if (index < height):

            new[index, column] += val - (div * max)
            index +=1
        else:
            column +=1
            index = 0
            new[index, column] += val - (div * max)
            index +=1
        if (index < height + 1):

            new[index, column] += 0
            index +=1
        else:
            column +=1
            index = 0
            new[index, column] += 0
            index +=1

        
    return new

file = open('data.txt',mode='r')
my = file.read()

print(len(my))

img = cv.imread('black4k.jpg', 0)
plt.imshow(encrypt(img, my, 5))

plt.show()


            

