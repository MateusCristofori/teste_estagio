distancia = 100
velocidade_carro = 110
velocidade_caminhao = 80
tempo_pedagio = 0.0833

# Calculando o tempo de viagem de cada veículo até o ponto de encontro
encontro_carro = distancia / 2 / velocidade_carro 
encontro_caminhao = distancia / 2 / velocidade_caminhao + 2 * tempo_pedagio

# Calculando a distância percorrida por cada veículo até o ponto de encontro
dist1 = velocidade_carro * encontro_carro
dist2 = velocidade_caminhao * encontro_caminhao

# Calculando a distância entre o ponto de encontro e Ribeirão Preto, e entre o ponto de encontro e Franca
dist_rb = distancia / 2 - dist1
dist_fr = distancia / 2 - dist2

# Verificando qual veículo está mais próximo de sua cidade de origem
if dist_rb < dist_fr:
    print("O carro estará mais próximo de Ribeirão Preto.")
else:
    print("O caminhão estará mais próximo de Franca.")