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

def unmap(array):
    charList = string.printable
    s = ""
    for i  in range(len(array)):
        s += charList[array[i] - 1]
    return s

