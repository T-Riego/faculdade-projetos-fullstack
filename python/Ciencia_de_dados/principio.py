# Implementar uma solução em Python para estudar o comportamento de uma série temporal com Regressão Linear.
# A Regressão linear ajuda a idenficar uma tendencia.

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x= np.array([5,10,15,20,25,30,35,40,45,50]).reshape((-1,1))
y= np.array([6,12,14,23,25,31,29,38,45,49])

model= LinearRegression().fit(x,y) 

y_pred= model.predict(x) 
print('Dados de teste', y_pred, sep='\n')
print('Dados da predição:', y_pred, sep='\n' )

plt.scatter(x,y, color='blue')
plt.plot(x, y_pred, color='red')
plt.legend(['Predição', 'Dados reais'])
plt.show()