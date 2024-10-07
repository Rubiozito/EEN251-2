# Fliperama Super Sergio Run

Este repositório contém o código e as instruções para um sistema de jogo de fliperama utilizando o Raspberry Pi. O sistema integra um display OLED, botões para interação e uma tablea com as pontuações mais recentes além do record.

![Grupo](https://github.com/Rubiozito/EEN251-2/blob/main/foto_grupo.jpeg?raw=true)

## Funcionalidades

- **Display OLED**: Visualização do jogo.
- **Botões**: Controla as ações do jogo.
- **Tabela de pontos**: Mostra os pontos da últimas rodadas, além da maior pontuação geral e a maior da última hora.

## Componentes

| Item                          | Qtd |
| ----------------------------- | :-: |
| Raspberry Pi B Plus           |  1  |
| Botão                         |  2  |
| Display Raspberry PI 7" Touch |  1  |

## Diagrama de Blocos

![Diagrama de blocos](https://github.com/Rubiozito/EEN251-2/blob/main/diagrama.png?raw=true)

## Uso

- **Iniciar Sistema**
- **Iniciar Jogo**: Apertar um dos botões para iniciar o jogo.
- **Jogando**: Apertar o Botão A para pular e B para abaixar, utilize essas ações para desviar dos obstáuclos.
- **Reiniciar Jogo**: Após morrer, é possível apertar algum dos botões para jogar novamente.
- **Verificar Tabela de ponto**: É possível acessar a tabela de pontos para ver as pontuações.

## Visão Geral do Código

O código do jogo foi feito utilizando a biblioteca pygame, feita para criar jogos em python, o jogo pega os inputs definidos e carrega as imagens da pasta assets durante o jogo.
Ao final de caga rodada, após morrer é feita uma requisição http que envia as informações para serem exibidas no dashboard, exibindo as pontuações dos últimos jogos

Link para o dashboard:
https://stem.ubidots.com/app/dashboards/public/dashboard/EBX3TRN8F0DXvuYiQVPNced0nZK0HrnqN3WC_JaqZlE?navbar=true&contextbar=false

É possível encontrar o vídeo de apresentação do projeto no link abaixo:
https://github.com/Rubiozito/EEN251-2/blob/main/video_projeto.mp4

## Licença

Este projeto é de código aberto e está disponível sob a Licença MIT.

Para mais detalhes, consulte o [repositório do projeto](https://github.com/Rubiozito/EEN251-2).
