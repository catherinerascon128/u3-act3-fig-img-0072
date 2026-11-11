import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 
# catherine rascon NC = 0072
print("catherine rascons NC = 0072")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imag = cv2.imread("girasol.jpg")
plt.imshow(mi_imag)
plt.title("girasol y catherine rascon 0072")
plt.show()

print("-+-+-+-+-+ puntos sobre la imagen +-+-+-+-+")
plt.imshow(mi_imag)
x = [100,100,300,500]
y = [100,400,500,200],
plt.scatter(x, y, s=20,c="red")
plt.show()

print("-+-+-+-+-+ cuadro azul en la imagen +-+-+-+-+")
img_girasol = cv2.imread("girasol.jpg")
plt.imshow(img_girasol)
# x = [100,100,500,500,100]
# y = [500,100,100,500,500]
x = [300,300,650,650,100]
y = [500,100,100,400,400]
plt.plot(x, y, c="blue")
plt.show()

print("-+-+-+-+-+ circulo azul en la imagen +-+-+-+-+")
img_girasol = cv2.imread("girasol.jpg")
plt.imshow(img_girasol)
n = 30 # lados del poligono
x = np.zeros((n+1,))
y = np.zeros((n+1,))
(xc,yc) = (340,320)
r = 150 # radio
for img_girasol in range (n+1):
    t = 2*np.pi/n*img_girasol
    x[img_girasol]= xc + r*np.cos(t)
    y[img_girasol]= yc + r*np.sin(t)
plt.plot(x, y, c="green")
plt.show()
