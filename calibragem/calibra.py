
import scipy
from scipy.linalg import pinv as inv
import numpy as np

def MMQ(y, mx):
    # Calcula os coeficientes da regressão usando o método dos mínimos quadrados
    # mx: matriz de design (com as variáveis independentes)
    # y: vetor de variável dependente
    coef = inv(mx.T @ mx) @ (mx.T @ y) # Faz a linearização com os dados
    return coef

def RMSE(yReal, yEstimado):
    # Calcula a raiz do erro médio quadrático (RMSE)
    # yReal: vetor de valores reais
    # yEstimado: vetor de valores estimados
    residuos = np.sqrt(np.sum(np.power((yReal - yEstimado),2)) / len(yReal))
    return residuos

# Carrega os dados a partir do arquivo '/caminho/dados.txt'
input_data = np.loadtxt('/home/stephan/Documents/PlatformIO/Projects/sonar/calibragem/dados.txt', delimiter=',')
x = input_data[:, 0]
y = input_data[:, 1]

print("-" * 100)

# Regressão linear
tam = len(x) # Quantidade de valores analisados
mx = np.column_stack((x, np.ones(tam))) # Adiciona uma coluna de uns para a interceptação
a, b = MMQ(y, mx)
yEstimado = a * x + b # Y estimado
print("Coeficientes para modelo de regressão linear:", a, b)
print("RMSE:", RMSE(y, yEstimado))

print("-" * 100)

# Regressão quadrática
mx = np.column_stack((x**2, x, np.ones(tam))) # Adiciona colunas para x^2 e uma coluna de uns
a, b, c = MMQ(y, mx)
yEstimado = a * x**2 + b * x + c # Y estimado
print("Coeficientes para modelo de regressão quadrática:", a, b, c)
print("RMSE:", RMSE(y, yEstimado))

print("-" * 100)

# Regressão cúbica
mx = np.column_stack((x**3, x**2, x, np.ones(tam))) # Adiciona colunas para x^3, x^2 e uma coluna de uns
a, b, c, d = MMQ(y, mx)
yEstimado = a * x**3 + b * x**2 + c * x + d # Y estimado
print("Coeficientes para modelo de regressão cúbica:", a, b, c, d)
print("RMSE:", RMSE(y, yEstimado))