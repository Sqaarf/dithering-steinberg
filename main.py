import numpy as np
from PIL import Image
from tqdm import tqdm

img = Image.open('./images/landscape.jpg')
array = np.array(img)
shape = array.shape

factor = int(input("Factor :"))

def quant_err(color, coeff, err):
	c = color #The color of the pixel given in RGB format
	r = color[0] #Red value
	g = color[1] #Green value
	b = color[2] #Blue value
	r = r + err[0] * coeff/16
	g = g + err[1] * coeff/16
	b = b + err[2] * coeff/16
	return [r,g,b] #Returning the quantized error of the pixel

for y in tqdm(range(array.shape[1]-1)):
	for x in range(1, array.shape[0]-1):
		#Selecting the individual color values RGB
		oldR = array[x][y][0]
		oldG = array[x][y][1]
		oldB = array[x][y][2]

		#Finding if the pixel color is more close to black or white
		newR = round(factor * oldR/255) * (255/factor)
		newG = round(factor * oldR/255) * (255/factor)
		newB = round(factor * oldR/255) * (255/factor)

		array[x][y] = [newR, newG, newB]

		#Calculating the error by substracting the old color values to the new
		errR = oldR - newR
		errB = oldG - newG
		errG = oldG - newG
		err = (errR, errB, errG)

		array[x+1][y] = quant_err(array[x+1][y], 7, err) #Pushing the error into x+1, y pixel
		array[x-1][y+1] = quant_err(array[x-1][y+1], 3, err) #Pushing the error into x-1, y+1 pixel
		array[x][y+1] = quant_err(array[x][y+1], 5, err) #Pushing the error into x, y+1 pixel
		array[x+1][y+1] = quant_err(array[x+1][y+1], 7, err) #Pushing the error into x+1, y+1 pixel

invimg = Image.fromarray(array)
invimg.save('./images/dithered.png')
print("done.")
