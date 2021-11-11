import numpy as np
from PIL import Image
from tqdm import tqdm

img = Image.open('./images/landscape.jpg')
array = np.array(img)
shape = array.shape

factor = int(input("Factor :"))

def quant_err(color, coeff, err):
	c = color
	r = color[0]
	g = color[1]
	b = color[2]
	r = r + err[0] * coeff/16
	g = g + err[1] * coeff/16
	b = b + err[2] * coeff/16
	return [r,g,b]

for y in tqdm(range(array.shape[1]-1)):
	for x in range(1, array.shape[0]-1):
		oldR = array[x][y][0]
		oldG = array[x][y][1]
		oldB = array[x][y][2]

		newR = round(factor * oldR/255) * (255/factor)
		newG = round(factor * oldR/255) * (255/factor)
		newB = round(factor * oldR/255) * (255/factor)

		array[x][y] = [newR, newG, newB]

		errR = oldR - newR
		errB = oldG - newG
		errG = oldG - newG
		err = (errR, errB, errG)

		array[x+1][y] = quant_err(array[x+1][y], 7, err)
		array[x-1][y+1] = quant_err(array[x-1][y+1], 3, err)
		array[x][y+1] = quant_err(array[x][y+1], 5, err)
		array[x+1][y+1] = quant_err(array[x+1][y+1], 7, err)

invimg = Image.fromarray(array)
invimg.save('./images/dithered.png')
print("done.")
