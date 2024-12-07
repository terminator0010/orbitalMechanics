clc;                % Limpa a janela de comando
clear;              % Remove todas as variáveis do workspace
close all;          % Fecha todas as janelas de figuras abertas

% Constantes universais
G = 6.67430e-11; % Constante gravitacional em m^3 kg^-1 s^-2

% Funções para cálculos
velocidade_orbital = @(massa_central, raio_orbital) sqrt(G * massa_central / raio_orbital);
periodo_orbital = @(massa_central, raio_orbital) ...
    (2 * pi * raio_orbital) / velocidade_orbital(massa_central, raio_orbital);

% Parâmetros do sistema
massa_terra = 5.972e24; % Massa da Terra em kg
raio_orbital = 8000000; % Raio orbital em metros
inclination = 30; % Inclinação da órbita em graus

% Cálculos principais
velocidade = velocidade_orbital(massa_terra, raio_orbital);
periodo = periodo_orbital(massa_terra, raio_orbital);

% Parâmetros de tempo
delta_t = 60; % Intervalo de tempo em segundos
total_time = floor(periodo); % Tempo total para uma órbita completa
theta_values = linspace(0, 2 * pi, total_time / delta_t);

% Configuração do Gráfico
figure;
hold on;
grid on;
axis equal;
xlim([-raio_orbital * 1.2, raio_orbital * 1.2]);
ylim([-raio_orbital * 1.2, raio_orbital * 1.2]);
zlim([-raio_orbital * 1.2, raio_orbital * 1.2]);

% Desenhar a Terra
[x_terra, y_terra, z_terra] = sphere(50);
surf(6371000 * x_terra, 6371000 * y_terra, 6371000 * z_terra, ...
    'FaceColor', 'blue', 'EdgeColor', 'none', 'DisplayName', 'Terra');

% Desenhar a órbita
theta_orbita = linspace(0, 2 * pi, 1000);
x_orbita = raio_orbital * cos(theta_orbita);
y_orbita = raio_orbital * sin(theta_orbita);
z_orbita = raio_orbital * sind(inclination) * sin(theta_orbita);
plot3(x_orbita, y_orbita, z_orbita, '--', 'Color', [0.5, 0.5, 0.5], 'DisplayName', 'Órbita');

% Desenhar o objeto em órbita
objeto = plot3(raio_orbital, 0, 0, 'ro', 'MarkerSize', 8, 'DisplayName', 'Objeto em Órbita');

% Legendas e rótulos
legend;
xlabel('X (m)');
ylabel('Y (m)');
zlabel('Z (m)');
title('Animação de Órbita em 3D');

% Loop infinito para animação contínua
while true
    for i = 1:length(theta_values)
        theta = theta_values(i);
        x = raio_orbital * cos(theta);
        y = raio_orbital * sin(theta);
        z = raio_orbital * sind(inclination) * sin(theta); % Inclinação da órbita
        set(objeto, 'XData', x, 'YData', y, 'ZData', z);
        pause(0.05); % Intervalo para animação
    end
end
