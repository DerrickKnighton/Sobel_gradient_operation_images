# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:27:12 2019

@author: Derrick
"""
import cv2
import numpy as np



def convolution(paddedImg,Mask):
    #print(np.shape(paddedImg))
    #print(type(paddedImg))
    AfterDeriv = np.zeros((np.shape(paddedImg)[0] - 1,np.shape(paddedImg)[1] - 1))
    #print(type(xMask))
    #print(xMask[0][1])
    x = 1
    y = 1
    #iterate through every pixel except padded zeros on outside of image 
    while x <= np.shape(paddedImg)[0] - 2:
        y = 1
        
        while y <= np.shape(paddedImg)[1] - 2:
            
            currPixelMatrix = np.array([[paddedImg[x-1][y-1],paddedImg[x-1][y],paddedImg[x-1][y+1]],
                                        [paddedImg[x][y-1],paddedImg[x][y],paddedImg[x][y+1]],
                                        [paddedImg[x+1][y-1],paddedImg[x+1][y],paddedImg[x+1][y+1]]])
            
            temp = np.multiply(currPixelMatrix, Mask)
            AfterDeriv[x][y] = temp.sum()
            y += 1
        
        x += 1
        
    return AfterDeriv  


def Combine_Gradient(img1,img2):
    x = 0
    y = 0
    print(type(img1[x][y]))
    final_Image = np.zeros((np.shape(img1)[0],np.shape(img1)[1]))
    
    while x < np.shape(img1)[0]:
        
        while y < np.shape(img1)[1]:
            temp = ((img1[x][y]*img1[x][y])+(img2[x][y]*img2[x][y]))**(.5)
            final_Image[x][y] = int(temp)
            y += 1
        y = 0
        x += 1

    return final_Image

if __name__ == "__main__":
    img = cv2.imread('earl.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    paddedImg = np.pad(gray,(1,1),'constant')
    #print(paddedImg)
    
    xMask = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
    result_image = convolution(paddedImg,xMask)
    
    yMask = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
    result_image2 = convolution(paddedImg,xMask)
    
    final_Image = Combine_Gradient(result_image,result_image2)
    print("here")
    cv2.imwrite('task2_result.jpg',final_Image)