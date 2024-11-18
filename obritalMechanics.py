import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 6.67430e-11  # Constante gravitacional em m³/(kg s²)

class Satelite:
    def __init__(self, massa_central, massa_satelite, posicao_inicial, velocidade_inicial):
        self.massa_central = massa_central
        self.massa_satelite = massa_satelite
        self.posicao = np.array(posicao_inicial, dtype=float)
        self.velocidade = np.array(velocidade_inicial, dtype=float)

    def calcular_forca_gravitacional(self):
        distancia = np.linalg.norm(self.posicao)
        direcao = -self.posicao / distancia  # Vetor unitário na direção da força gravitacional
        forca_magnitude = G * self.massa_central * self.massa_satelite / distancia**2
        return forca_magnitude * direcao

    def atualizar_posicao_e_velocidade(self, delta_t):
        # Calcula a aceleração gravitacional
        forca_gravitacional = self.calcular_forca_gravitacional()
        aceleracao = forca_gravitacional / self.massa_satelite

        # Atualiza a velocidade e posição
        self.velocidade += aceleracao * delta_t
        self.posicao += self.velocidade * delta_t

massa_terra = 5.972e24  # Massa da Terra em kg
massa_satelite = 1000  # Massa do satélite em kg
posicao_inicial = [7000e3, 0]  # Posição inicial (exemplo em órbita baixa a 7000 km do centro da Terra)
velocidade_inicial = [0, 7500]  # Velocidade inicial (m/s perpendicular à posição)

satelite = Satelite(massa_terra, massa_satelite, posicao_inicial, velocidade_inicial)

# Parâmetros de tempo
delta_t = 10  # Intervalo de tempo em segundos
total_time = 3600 * 3  # Tempo total da simulação em segundos

# Configuração da animação
fig, ax = plt.subplots()
ax.set_aspect('equal')
limite = np.linalg.norm(posicao_inicial) * 1.5
ax.set_xlim(-limite, limite)
ax.set_ylim(-limite, limite)

# Terra e satélite
terra = plt.Circle((0, 0), 6371e3, color='blue', label='Terra')  # Raio da Terra em metros
ax.add_artist(terra)
objeto, = ax.plot([], [], 'ro', label='Satélite')
trilha, = ax.plot([], [], 'r-', alpha=0.5, linewidth=0.5)

# Listas para armazenar dados da trilha
posicoes_x, posicoes_y = [], []

def update(frame):
    # Atualiza posição e velocidade do satélite
    satelite.atualizar_posicao_e_velocidade(delta_t)
    
    # Armazena a posição para a trilha
    posicoes_x.append(satelite.posicao[0])
    posicoes_y.append(satelite.posicao[1])
    
    # Atualiza os dados do satélite e da trilha na animação
    objeto.set_data([satelite.posicao[0]], [satelite.posicao[1]])  # Passa como listas
    trilha.set_data(posicoes_x, posicoes_y)
    
    return objeto, trilha

# Animação
ani = animation.FuncAnimation(fig, update, frames=total_time // delta_t, interval=50, blit=True)

plt.legend()
plt.show()
