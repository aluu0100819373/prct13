#!/usr/bin/python
#!encoding: UTF-8
import matplotlib.pylab as pl
import numpy as np
import listas

error=listas.lista()
print error


valoresX = [1, 2, 3 ,7, 5]
umbral=(1.e-4, 1.e-5, 1.e-6, 1.e-7, 1.e-8)
intervalo=(10,50,100,150,1000)

plot0 = pl.plot(valoresX,error[1],'bp', label='error1')
plot1 = pl.plot(valoresX,error[2],'rp', label='error2')
plot2 = pl.plot(valoresX,error[3],'mp', label='error3')
plot3 = pl.plot(valoresX,error[4],'yp', label='error4')
# Incluir un título
pl.title('Dibujar x frente a y')

# Poner etiquetas en los ejes
pl.xlabel('Algunos enteros positivos')
pl.ylabel('Cuadrado y doble de algunos enteros')

# Poner limites a los ejes
pl.xlim(0.0,7.0)
pl.ylim(-10.0,110.0)
pl.xticks(valoresX,
	  [1.e-4, 1.e-5, 1.e-6, 1.e-7, 1.e-8])
#pl.yticks([10,20,30,40],    [0])

pl.legend(loc=2, numpoints=1)

pl.show()


