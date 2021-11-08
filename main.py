import numpy as np
from PIL import Image

img = Image.open('./images/Guts.png')
array = np.array(img)
shape = array.shape

factor = 4

for y in range(array.shape[1]-1):
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

		c = array[x+1][y]
		r = array[x+1][y][0]
		g = array[x+1][y][1]
		b = array[x+1][y][2]
		r = r + errR * 7/16
		g = g + errG * 7/16
		b = b + errB * 7/16
		array[x+1][y] = [r,g,b]

		c = array[x-1][y+1]
		r = array[x-1][y+1][0]
		g = array[x-1][y+1][1]
		b = array[x-1][y+1][2]
		r = r + errR * 3/16
		g = g + errG * 3/16
		b = b + errB * 3/16
		array[x-1][y+1] = [r,g,b]

		c = array[x][y+1]
		r = array[x][y+1][0]
		g = array[x][y+1][1]
		b = array[x][y+1][2]
		r = r + errR * 5/16
		g = g + errG * 5/16
		b = b + errB * 5/16
		array[x][y+1] = [r,g,b]

		c = array[x+1][y+1]
		r = array[x+1][y+1][0]
		g = array[x+1][y+1][1]
		b = array[x+1][y+1][2]
		r = r + errR * 7/16
		g = g + errG * 7/16
		b = b + errB * 7/16
		array[x+1][y+1] = [r,g,b]

invimg = Image.fromarray(array)
invimg.save('./images/test.png')
print("done.")