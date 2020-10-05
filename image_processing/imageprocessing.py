import cImage 
import sys


# apply negative filter #
def negativeImage(sourceImg):
	newImg = cImage.EmptyImage(sourceImg.getWidth(),sourceImg.getHeight())

	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x,y)
			negativeP = cImage.Pixel(255-p.getRed(), 255-p.getGreen(), 255-p.getBlue())
			newImg.setPixel(x, y, negativeP)

	return newImg

# gray Scale #
def grayScale(sourceImg):
	newImg = cImage.EmptyImage(sourceImg.getWidth(),sourceImg.getHeight())

	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x,y)
			intensity = (p.getRed() + p.getGreen() + p.getBlue()) // 3
			grayP = cImage.Pixel(intensity, intensity, intensity)
			newImg.setPixel(x, y, grayP)

	return newImg


# two times bigger #
def double(sourceImage):
	newImg = cImage.EmptyImage(2*sourceImage.getWidth(), 2*sourceImage.getHeight())

	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x, y)
			for i in range(2):
				for j in range(2):
					newImg.setPixel(2*x+i, 2*y+j, p)
	return newImg


# factor is how many times bigger #            
def enlarge(sourceImg, factor):
	newImg = cImage.EmptyImage(factor*sourceImg.getWidth(), factor*sourceImg.getHeight())

	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x, y)
			for i in range(factor):
				for j in range(factor):
					newImg.setPixel(factor*x+i, factor*y+j, p)
	return newImg

# flip the image horizontally #
def horizontalFlip(sourceImg):
	newImg = cImage.EmptyImage(sourceImg.getWidth(), sourceImg.getHeight())
	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x,y)
			newImg.setPixel(sourceImg.getWidth()-1-x, y, p)

	return newImg

# flip the image vertically #
def verticalFlip(sourceImg):
	newImg = cImage.EmptyImage(sourceImg.getWidth(), sourceImg.getHeight())
	for x in range(sourceImg.getWidth()):
		for y in range(sourceImg.getHeight()):
			p = sourceImg.getPixel(x,y)
			newImg.setPixel(x,sourceImg.getHeight()-1-y,p)

	return newImg




def main():
	fileName = sys.argv[1]
	
	imageToProcess = cImage.FileImage(fileName)

	print('What would you like to do?')
	print('1) Negative')
	print('2) Gray Scale')
	print('3) Multiply picture size')
	print('4) Horizontal Flip')
	print('5) Vertical Flip')

	choice = input('Please pick an operation (1-4):')

	if choice == '1':
		newImg = negativeImage(imageToProcess)
	elif choice == '2':
		newImg = grayScale(imageToProcess)
	elif choice == '3':
		mult = int(input('Multiply picture size by: '))
		newImg = enlarge(imageToProcess, mult)

	if choice != '3':
		myImageWin = cImage.ImageWin('Image Processing', 2*imageToProcess.getWidth()+10,\
								 imageToProcess.getHeight())
	else:
		myImageWin = cImage.ImageWin('Image Processing', mult*2*imageToProcess.getWidth(),\
									 imageToProcess.getHeight()*mult)
	if choice == '4':
		newImg = horizontalFlip(imageToProcess)

	if choice == '5':
		newImg = verticalFlip(imageToProcess)
	
	imageToProcess.draw(myImageWin)

	newImg.setPosition(imageToProcess.getWidth()+10,0)

	newImg.draw(myImageWin)

	myImageWin.exitonclick()


main()
