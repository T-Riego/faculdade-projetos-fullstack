#Carregar dados da base load_digits. informar a quantidade de dados.
#visualizar os sdados carregados.
#Utilizar um modelo de regressao logistica.
# 
# 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
digitos= load_digits()

print("Shape dos dados de imagens:".format(digitos.data.shape))
print("Shape dos dados de target:".format(digitos.target.shape))

plt.figure(figsize=(14,4))
for index, (imagem,rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
    plt.subplot(1,5,index+1)
    plt.imshow(np.reshape(imagem,(8,8)), cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Label: %i\n' % rotulo, fontsize=20)

x_treino, x_teste, y_treino, y_teste = train_test_split(digitos.data,
                                                        digitos.target,
                                                        test_size=0.25,
                                                        random_state=0)

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

pipe = make_pipeline(StandardScaler(),
                     LogisticRegression())

pipe.fit(x_treino, y_treino)

Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
previsto = pipe.predict(x_teste[0].reshape(1, -1))
real = y_teste[0]
print('previsto:{}; real:{}'.format(previsto[0], real))

# Saída do código:
# previsto:2; real:2