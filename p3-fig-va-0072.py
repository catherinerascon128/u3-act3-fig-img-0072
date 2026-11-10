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