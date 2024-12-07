import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constantes universais
G = 6.67430e-11  # Constante gravitacional em m^3 kg^-1 s^-2

# Função para calcular a velocidade orbital
def velocidade_orbital(massa_central, raio_orbital):
    return np.sqrt(G * massa_central / raio_orbital)

# Função para calcular o período orbital
def periodo_orbital(massa_central, raio_orbital):
    velocidade = velocidade_orbital(massa_central, raio_orbital)
    circunferencia_orbital = 2 * np.pi * raio_orbital
    return circunferencia_orbital / velocidade

# Parâmetros do sistema (usando a Terra como exemplo)
massa_terra = 5.972e24  # Massa da Terra em kg
raio_orbital = 8000000  # Raio orbital a 300 km acima da Terra em metros

# Calcular velocidade e período orbital
velocidade = velocidade_orbital(massa_terra, raio_orbital)
periodo = periodo_orbital(massa_terra, raio_orbital)

# Parâmetros de tempo para a simulação
delta_t = 60  # Intervalo de tempo em segundos (1 minuto)
total_time = int(periodo)  # Tempo total para uma órbita completa

# Inicializar dados de posição
theta_values = np.arange(0, 2 * np.pi, 2 * np.pi / (total_time / delta_t))

# Configuração da animação
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-raio_orbital * 1.1, raio_orbital * 1.1)
ax.set_ylim(-raio_orbital * 1.1, raio_orbital * 1.1)

# Desenhar a Terra
terra = plt.Circle((0, 0), 6371000, color='blue', label='Terra')
ax.add_artist(terra)

# Desenhar a órbita
orbita = plt.Circle((0, 0), raio_orbital, color='grey', fill=False, linestyle='--')
ax.add_artist(orbita)

# Desenhar o objeto em órbita
objeto, = ax.plot([], [], 'ro', label='Objeto em órbita')

# Função para atualizar a posição do objeto
def update(i):
    theta = theta_values[i]
    x = raio_orbital * np.cos(theta)
    y = raio_orbital * np.sin(theta)
    objeto.set_data([x], [y])  # Passar x e y como listas
    return objeto,

# Criar a animação
ani = animation.FuncAnimation(fig, update, frames=len(theta_values), interval=50, blit=True)

# Mostrar o gráfico com animação
plt.legend()
plt.show()
