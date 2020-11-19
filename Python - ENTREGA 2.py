from math import radians, sin, cos, tan
import matplotlib.pyplot as plt
import time
from datetime import datetime

angulosFormacoesRochosas = [30, 45, 60]

w = 1  # Define a frequência em segundos
x = len(angulosFormacoesRochosas)  # Quantidade de formações rochosas
y = 5  # Define a distância da base até as formações rochosas
z = 1  # Define a velocidade em metros por segundo m/s


def desenhar(anguloCotovelo, larguraL1, anguloBroca, larguraL2, titulo):
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
    fileName = 'report' + str(datetime.now().strftime("%H%M%S"))
    plt.title(fileName + ' - cotovelo : ' + str(anguloCotovelo) +
              '° - broca : ' + str(anguloBroca) + '°')
    try:
        plt.savefig('C:/teste/' + fileName + '.png')
        # plt.show()
    except:
        print('some error ...')


posicaoDescanso = [90, -45]

for i in range(len(angulosFormacoesRochosas)):
    print('------------------------------------------------------------------------------')
    startTime = datetime.now().strftime("%H:%M:%S")
    print('Início da missão ' + str(i+1) + ' : ' +str(startTime))
    print('Posição de descanso - ' + 'Cotovelo: ' + str(posicaoDescanso[0]) + '° Broca: ' + str(posicaoDescanso[1]) + '°')
    localizacaoAtual = 0
    print('------------------------------------------------------------------------------')
    while localizacaoAtual < y:
        print('Distância até as formações rochosas : ' + str(y - localizacaoAtual) + ' metros | Velocidade : ' + str(z) + 'm/s')
        localizacaoAtual += z
        time.sleep(w)
    if(localizacaoAtual > y):
        localizacaoAtual = y
    print('Distância até as formações rochosas : ' + str(y - localizacaoAtual) + ' metros')
    print('------------------------------------------------------------------------------')
    print('Posicionando o braço robótico na formação rochosa ' + str(i+1))
    posicaoAtual = posicaoDescanso
    print('Cotovelo: ' + str(posicaoAtual[0]) + ' | Broca: ' + str(posicaoAtual[1]))
    while posicaoAtual[0] > angulosFormacoesRochosas[i] or posicaoAtual[1] < angulosFormacoesRochosas[i]:
        if posicaoAtual[0] > angulosFormacoesRochosas[i]:
            posicaoAtual[0] -= w
        if posicaoAtual[1] < angulosFormacoesRochosas[i]:
            posicaoAtual[1] += w
        print('Cotovelo: ' + str(posicaoAtual[0]) + ' | Broca: ' + str(posicaoAtual[1]))
        time.sleep(w)
    print('Iniciando retirada de amostras ...')
    print('Voltando para a base ...')
    print('------------------------------------------------------------------------------')
    while localizacaoAtual > 0:
        print('Distância até a base : ' + str(localizacaoAtual) + ' metros | Velocidade : ' + str(z) + 'm/s')
        localizacaoAtual -= z
        time.sleep(w)
    localizacaoAtual = 0
    print('Distância até a base : ' + str(localizacaoAtual) + ' metros | Velocidade : ' + str(z) + 'm/s')
    posicaoDescanso = [90, -45]
print('Congragulations mission complete')