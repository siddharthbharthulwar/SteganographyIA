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

        val = mapped[i]
        div = truncate(val / max)
        print(div)
        for j in range(div):
            print(column)
            if (index < height):
                new[index, column] += max
                index +=1
            else:
                column +=1
                index = 0
                new[index, column] += max
                index +=1
        new[index, column] = new[index, column]
        index +=1
        
    return new

file = open('data.txt',mode='r')
my = file.read()

img = cv.imread('clyde.jpg', 0)
plt.imshow(encrypt(img, my, 20))

plt.show()


            

