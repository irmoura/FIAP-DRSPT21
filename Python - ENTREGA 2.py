from math import radians, sin, cos, tan
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
from pathlib import Path

angulosFormacoesRochosas = [30, 45, 60] #Vetor contendo o angulo de cada formação rochosa
passo = 5

w = 1  # Define a frequência em segundos do feedback
x = len(angulosFormacoesRochosas)  # Quantidade de formações rochosas
y = 50  # Define a distância da base até as formações rochosas
z = 5  # Define a velocidade em metros por segundo m/s


def desenhar(anguloCotovelo, larguraL1, anguloBroca, larguraL2, registro):
    yCotovelo = sin(radians(anguloCotovelo))
    xCotovelo = cos(radians(anguloCotovelo))
    yBroca = sin(radians(anguloBroca))
    xBroca = cos(radians(anguloBroca))
    xCotovelo = larguraL1*xCotovelo
    yCotovelo = larguraL1*yCotovelo
    xBroca = larguraL2*xBroca
    yBroca = larguraL2*yBroca
    xBroca = xCotovelo+xBroca
    yBroca = yCotovelo+yBroca
    plt.figure()
    plt.plot([0, xCotovelo], [0, yCotovelo])
    plt.plot([xCotovelo, xBroca], [yCotovelo, yBroca])
    plt.plot([0], [0], '-ro')
    plt.plot([xCotovelo], [yCotovelo], '-go')
    plt.plot([xBroca], [yBroca], '-bo')
    plt.axis((-10, 20, -10, 20))
    fileName = 'FeedBack ' + str(registro)
    plt.title(fileName + ' - cotovelo : ' + str(anguloCotovelo) +
              '° - broca : ' + str(anguloBroca) + '°')
    try:
        caminho = str(Path.home()) + '\\Downloads\\Rover\\' #Irá criar uma pasta chamada Rover em Downloads contendo os gráficos
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        plt.savefig(caminho + fileName + '.png')
        # plt.show()
    except:
        print('some error ...')

posicaoDescanso = [90, -45] #Ângulo padrão de descanso, Cotovelo e broca respectivamente
count = 0

for i in range(len(angulosFormacoesRochosas)):
    print('\033[31m------------------------------------------------------------------------------\033[m')
    startTime = datetime.now().strftime("%H:%M:%S")
    print('Início da missão {} : {}'.format(str(i+1), str(startTime)))
    print('Posição de descanso - Cotovelo: {}° Broca: {}°'.format(str(posicaoDescanso[0]), str(posicaoDescanso[1])))
    localizacaoAtual = 0
    print('\033[31m------------------------------------------------------------------------------\033[m')
    while localizacaoAtual < y:
        if count == w:
            count = 0
            print('Distância até as formações rochosas : {} metros | Velocidade : {}m/s'.format(str(y - localizacaoAtual), str(z)))
        localizacaoAtual += z
        time.sleep(1)
        count += 1
    count = 1
    if(localizacaoAtual > y):
        localizacaoAtual = y
    print('Distância até as formações rochosas : {}'.format(str(y - localizacaoAtual)))
    print('\033[31m------------------------------------------------------------------------------\033[m')
    print('Posicionando o braço robótico na formação rochosa {} | Ângulo: {}'.format(str(i+1), str(angulosFormacoesRochosas[i])))
    posicaoAtual = posicaoDescanso
    print('Cotovelo: {}° | Broca: {}°'.format(str(posicaoAtual[0]), str(posicaoAtual[1])))
    while posicaoAtual[0] > angulosFormacoesRochosas[i] or posicaoAtual[1] < angulosFormacoesRochosas[i]:
        if posicaoAtual[0] > angulosFormacoesRochosas[i]:
            posicaoAtual[0] -= passo
        if posicaoAtual[1] < angulosFormacoesRochosas[i]:
            posicaoAtual[1] += passo
        if count == w:
            count = 0
            print('Cotovelo: {}° | Broca: {}°'.format(str(posicaoAtual[0]), str(posicaoAtual[1])))
        time.sleep(1)
        count += 1
    count = 1
    print('Iniciando retirada de amostras ...')
    print('Voltando para a base ...')
    print('\033[31m------------------------------------------------------------------------------\033[m')
    while localizacaoAtual > 0:
        print('Distância até a base : {} metros | Velocidade : {}m/s'.format(str(localizacaoAtual), str(z)))
        localizacaoAtual -= z
        time.sleep(1)
    localizacaoAtual = 0
    print('Distância até a base : {} metros | Velocidade : {}m/s'.format(str(localizacaoAtual), str(z)))
    posicaoDescanso = [90, -45]
print('Congragulations mission complete')