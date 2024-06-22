import matplotlib
matplotlib.use('Qt5Agg')  # Usar backend Qt5Agg para exibir o gráfico
import matplotlib.pyplot as plt

# Dados das leituras sem filtrar (substitua os valores abaixo pelos seus dados)
parametros = [10, 30, 50, 70, 90, 110]
distancias_sem_filtrar = [9.3, 28.9, 48.4, 67.9, 87.2, 108.3]
tempo_sem_filtrar = [1, 2, 3, 4, 5, 6]  # Valores de tempo correspondentes às leituras

# Dados das leituras filtradas (substitua os valores abaixo pelos seus dados)
distancias_filtradas = [9.6, 30.1, 48.8, 68.5, 89.5, 109]
tempo_filtrado = [1, 2, 3, 4, 5, 6]  # Valores de tempo correspondentes às leituras filtradas

# Plotar o gráfico das distâncias sem filtrar
plt.plot(tempo_sem_filtrar, distancias_sem_filtrar, label='Distância sem filtrar')

# Plotar o gráfico das distâncias filtradas
plt.plot(tempo_filtrado, distancias_filtradas, label='Distância filtrada')

# Adicionar legendas e título ao gráfico
plt.xlabel('Parâmetros (unidade)')
plt.ylabel('Distância (cm)')
plt.title('Leituras do Sensor Ultrassônico')
plt.legend()

# Exibir o gráfico
plt.show()
