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

def decrypt(img, encryptedimg):
    max = 0 #TODO: automatically encrypt and detect @MAX
    index = 0
    column = 0
    sub = np.abs(np.subtract(img, encryptedimg))
    plt.imshow(sub, cmap='gist_gray_r')
    plt.show()
    width = sub.shape[1]
    height = sub.shape[0]
    maxNotFound = True
    while (maxNotFound):
        if (sub[index, column] == 0):
            if (index < height):
                max +=1
                index +=1
            else:
                max +=1
                column +=1
                index = 0
                index +=1
        else:
            maxNotFound = False
    print(max)
    
    vals = []
    breakLoop = False
    while (column < width) and (index < height) and (len(vals) < 4):
        zeroHit = True
        val = 0
        while (zeroHit):
            if (sub[index, column] == 0):
                print(sub[index, column])
                if (index + 1< height):
                    #print("inside array")
                    #print(sub[index + 1, column])
                    print(index, column)
                    zeroHit = False
                    index +=1
                else:
                    #print("outside array")
                   # print(sub[0, column + 1])
                    print(index, column)
                    zeroHit = False
                    index = 0
                    column +=1
            else:
                if (index < height):
                 #   print("not zero, inside")
                    print(sub[index, column])
                    val += sub[index, column]
                    index +=1
                else:
                 #   print("not zero, outside array")
                    print(sub[index, column])
                    val += sub[index, column]
                    index = 0
                    column +=1

                    


    '''
    valList = []
    while (column < width) and (index < height):
        print(column, index)
        zeroHit = True
        val = 0
        while (zeroHit):
            if (sub[index, column] == 0):
                if (index < height):
                    if (sub[index + 1, column] == 0):
                        index +=1
                        zeroHit = False
                        print("zero hit hit")
                        valList.append(val)
                    
                    else:
                        if (sub[0, column + 1] == 0):
                            index = 0
                            column +=1
                            zeroHit = False
                            print("zero hit hit ")
                            valList.append(val)
                            index +=1
                    
            else:
                print(column, index)
                if (sub[index, column] == 1):
                    val += max
                    if (index < height):
                        index +=1
                    else:
                        index = 0
                        column +=1
                else:
                    val += sub[index, column]
                    
                    if (index < height):
                        index +=1
                    else:
                        index = 0
                        column +=1
    
    '''
    print(valList)
    return sub


print(string.printable)
img = cv.imread('black.png', cv.IMREAD_GRAYSCALE)
file = open('data.txt',mode='r')
my = file.read()
my = "9abcdefgh"
plt.imshow(img)
plt.show()

encrypted = encrypt(img, my, 13)
plt.imshow(encrypted)
plt.show()

plt.imshow(img)
plt.show()

plt.imshow(decrypt(img, encrypted))
plt.show()
