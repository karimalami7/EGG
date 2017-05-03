import numpy as np
import matplotlib.pyplot as plt




def plot(eleprop):

	x=list()
	y=list()

	for i in range (0,len(eleprop)):
		x.append(i)
		y.append(eleprop[i])

	plt.plot(x, y)
	plt.show() # affiche la figure a l'ecran