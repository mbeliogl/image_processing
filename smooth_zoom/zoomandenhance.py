

import cImage
import sys

def zoom(image, upperLeftX, upperLeftY, lowerRightX, lowerRightY, scalingFactor):
  
    newW = lowerRightX - upperLeftX
    newH = lowerRightY - upperLeftY
    
   
    newImg = cImage.EmptyImage(newW, newH)
    
    for x in range(upperLeftX, lowerRightX):
        for y in range(upperLeftY, lowerRightY):
            p = image.getPixel(x, y)
            newImg.setPixel(x-upperLeftX, y-upperLeftY, p)
    #creates a new image that will contain the zoomed region after it has been scaled#
    scaledImg = cImage.EmptyImage(newW * scalingFactor, newH * scalingFactor)
    # this for loop gets the original pixels and assigns it to the scaled pixels in the scaledImg#
    for x in range(newW):
        for y in range(newH):
            pixel = newImg.getPixel(x, y)
            for i in range(scalingFactor):
                for j in range(scalingFactor):
                    scaledImg.setPixel(x * scalingFactor + i, y * scalingFactor + j, pixel)

    return scaledImg
   

def restrict(num, minNum, maxNum):
    #restricts the possible range of numbers with if statements#
    if num < minNum:
        num = minNum
    if num > maxNum:
        num = maxNum
    return num

#sharpening the image 
def sharpenImage(image):
   
    w = image.getWidth()
    h = image.getHeight()
    sharpImage = cImage.EmptyImage(w, h)

    #transforming the original pixel 'p'#
    for x in range(1, w-1):
        for y in range(1, h-1):
            p = image.getPixel(x, y)
            #pInt is the intensity of the central pixel#
            pIntRed = 9 * p.getRed()
            pIntGreen = 9 * p.getGreen()
            pIntBlue = 9 * p.getBlue()

            #for loop that takes all surrounding pixels 'nearPix'#
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        pass
                    else:
                        nearPix = image.getPixel(x+i, y+j)
                        pIntRed = pIntRed-nearPix.getRed()
                        pIntGreen = pIntGreen-nearPix.getGreen()
                        pIntBlue = pIntBlue-nearPix.getBlue()
            #uses the restrict function#
            pIntRed = restrict(pIntRed, 0, 255)
            pIntGreen = restrict(pIntGreen, 0, 255)
            pIntBlue = restrict(pIntBlue, 0, 255)
            #assign new values to P#
            p.setRed(pIntRed)
            p.setGreen(pIntGreen)
            p.setBlue(pIntBlue)

            sharpImage.setPixel(x, y, p)

    return sharpImage
    

#displaying the processed image   
def main():
    
    filename = sys.argv[1]

    #Create two copies of the given image
    #One that we will draw a green box on
    image = cImage.FileImage(filename)
    imageCopy = cImage.FileImage(filename)

    #Display the given image
    originalWin = cImage.ImageWin("Original", image.getWidth(), image.getHeight())
    image.draw(originalWin)

    #Keeps asking the user to pick a region to zoom in on
    #until they make a valid choice
    picked = False
    while not picked:
        print("Please click the upper-left corner of the region")
        upperLeft = originalWin.getMouse()
        print("Please click the lower-right corner of the region")
        lowerRight = originalWin.getMouse()
        
        if lowerRight[0] < upperLeft[0] or lowerRight[1] < upperLeft[1]:
            print("Not a valid region")
        else:
            picked = True

    #Have to adjust the coordinates in the window to account for the white border created by cImage
    ulX = upperLeft[0] - 5
    ulY = upperLeft[1] - 5
    lrX = lowerRight[0] - 5
    lrY = lowerRight[1] - 5

    #Create a green pixel for drawing a box around the zoom region.
    boxPixel = cImage.Pixel(0, 255, 0)

    #Draw the top and bottom sides of the box
    for x in range(ulX, lrX + 1):
        if ulY > 0:
            image.setPixel(x, ulY - 1, boxPixel)
            
        if lrY < image.getHeight() - 1:
            image.setPixel(x, lrY + 1, boxPixel)

    #Draw the left and right sides of the box
    for y in range(ulY, lrY + 1):
        if ulX > 0:
            image.setPixel(ulX - 1, y, boxPixel)

        if lrX < image.getWidth() - 1:
            image.setPixel(lrX + 1, y, boxPixel)

    #Keeps asking the user for a scaling factor until they input something that is at least 1.
    scale = 0
    while scale <= 0:
        scale = int(input("Please pick a scaling factor (at least 1): "))

    print("Zooming and Enhancing...")
    
    #Sharpen the image ("enhance")
    enhanced = sharpenImage(imageCopy)
   
    #Zoom in on the specified region
    zoomed = zoom(enhanced, ulX, ulY, lrX, lrY, scale)

    #Display the enhanced and zoomed image
    zoomWin = cImage.ImageWin("Zoom...and Enhance!", zoomed.getWidth(), zoomed.getHeight())
    zoomed.draw(zoomWin)

    print("Click the zoom window to exit, when ready.")
    zoomWin.exitOnClick()

main()
    
