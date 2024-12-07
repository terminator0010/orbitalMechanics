% Constantes universais
G = 6.67430e-11; % Constante gravitacional em m^3 kg^-1 s^-2

% Função para calcular a velocidade orbital
velocidade_orbital = @(massa_central, massa_objeto, raio_orbital) sqrt(G * (massa_central + massa_objeto) / raio_orbital);

% Função para calcular o período orbital
periodo_orbital = @(massa_central, raio_orbital) ...
    (2 * pi * raio_orbital) / velocidade_orbital(massa_central, massa_objeto, raio_orbital);

% Parâmetros do sistema (usando a Terra como exemplo)
massa_terra = 5.972e24; % Massa da Terra em kg
massa_objeto = 10;
raio_orbital = 8000000; % Raio orbital a 300 km acima da Terra em metros

% Calcular velocidade e período orbital
velocidade = velocidade_orbital(massa_terra, massa_objeto, raio_orbital);
periodo = periodo_orbital(massa_terra, raio_orbital);

% Parâmetros de tempo para a simulação
delta_t = 60; % Intervalo de tempo em segundos (1 minuto)
total_time = floor(periodo); % Tempo total para uma órbita completa
theta_values = linspace(0, 2 * pi, total_time / delta_t);

% Configuração da animação
figure;
hold on;
axis equal;
xlim([-raio_orbital * 1.1, raio_orbital * 1.1]);
ylim([-raio_orbital * 1.1, raio_orbital * 1.1]);

% Desenhar a Terra
theta_terra = linspace(0, 2*pi, 100);
x_terra = 6371000 * cos(theta_terra); % Raio da Terra em metros
y_terra = 6371000 * sin(theta_terra);
fill(x_terra, y_terra, 'blue', 'DisplayName', 'Terra');

% Desenhar a órbita
theta_orbita = linspace(0, 2*pi, 100);
x_orbita = raio_orbital * cos(theta_orbita);
y_orbita = raio_orbital * sin(theta_orbita);
plot(x_orbita, y_orbita, '--', 'Color', [0.5, 0.5, 0.5], 'DisplayName', 'Órbita');

% Desenhar o objeto em órbita
objeto = plot(raio_orbital, 0, 'ro', 'MarkerSize', 8, 'DisplayName', 'Objeto em Órbita');

legend;

% Função para atualizar a posição do objeto
for i = 1:length(theta_values)
    theta = theta_values(i);
    x = raio_orbital * cos(theta);
    y = raio_orbital * sin(theta);
    set(objeto, 'XData', x, 'YData', y);
    pause(0.05); % Intervalo para animação
end
