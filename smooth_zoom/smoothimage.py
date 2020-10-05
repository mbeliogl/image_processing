
import sys
import cImage

def smoothImage(sourceImg):
    #creating the original image and the smooth image also sets the height and width#
    image = cImage.FileImage(sourceImg)
    w = image.getWidth()
    h = image.getHeight()
    smoothImg = cImage.EmptyImage(w, h)
# establishing edges in the new picture (image)#
    for x in range(w):
        p = image.getPixel(x, 0)
        smoothImg.setPixel(x, 0, p)
        smoothImg.setPixel(x, h-1, p)
        
    for y in range(h):
        p = image.getPixel(0, y)
        smoothImg.setPixel(0, y, p)
        smoothImg.setPixel(w-1, y, p)

#the entire for loop calculates the averages of the pixel values and sets them to new #
    for x in range(1, w-1):
        for y in range (1, h-1):
            p = image.getPixel(x, y)
            
            red = 0
            green = 0
            blue = 0
            # makes sure all surrounding pixels are in including the original#
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nearPix = image.getPixel(x+i, y+j) #near pix are pixels around the original #
                    red += nearPix.getRed()
                    green += nearPix.getGreen()
                    blue += nearPix.getBlue()
            #averages of 9 pixels #        
            red = red / 9
            green = green / 9
            blue = blue / 9
            # sets the values to int and assigns the pixes to new image #
            p.setRed(int(red))
            p.setGreen(int(green))
            p.setBlue(int(blue))
            smoothImg.setPixel(x, y, p)

    return smoothImg
            
                       
# the main function draws the images side by side #    
def main():
    fileName = sys.argv[1]
    # the image to process and its dimenstions #
    imageToProcess = cImage.FileImage(fileName)
    
    w = imageToProcess.getWidth()
    h = imageToProcess.getHeight()
    #creating a window that is double the size(width) to fit both pictures #
    myImageWin = cImage.ImageWin('Image Processing', 2.5 * w, h)

    imageToProcess.draw(myImageWin)
    imageToProcess = smoothImage(fileName)

    imageToProcess.setPosition(w + 50, 0)
    imageToProcess.draw(myImageWin)
    myImageWin.exitonclick()

main()
