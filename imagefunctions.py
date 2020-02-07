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

def encrypt(img, text, max):
    width = img.shape[1]
    height = img.shape[0]
    mapped = map(text)
    index = 0
    column = 0
    for i in range(len(mapped)):
        val = mapped[i]

        div = truncate(val / max)

        for j in range(div):
            if (index < height):
                print(index, column)
                img[index, column] +=1
                index +=1
            else:
                index = 0
                column +=1
                img[index, column] +=1
                index +=1

        if (index < height):
            img[index, column] += val - (truncate(val / max) * max)
            index +=1
        else:
            index = 0
            column +=1
            img[index, column] += val - (truncate(val / max) * max)
            index +=1
        
        if (index < height):
            img[index, column] = img[index, column]
            index +=1
        else:
            index = 0
            column +=1
            img[index, column] = img[index, column]
            index +=1
    return img

img = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
plt.imshow(encrypt(img, "hello world", 2))
plt.show()