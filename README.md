### Projeto Jogo da Velha Robótico.

O script jogo.py é o principal. Nele está a lógica do jogo, a implementação do jogo em interface gráfica e o comando para o robô realizar as jogadas em tabuleiro físico.

O projeto escolheu desenvolver a implementação dos movimentos do robô ao estabelecer um protótipo de robô, para que os testes de interface em jogo.py com um robô de teste minimizassem o impacto de código ao agregar o script do robô real. A classe AbstractRobot permite essa abordagem.

O robô de teste, na classe TestRobot, serve para depurar os estados esperados do robô com prints de mensagens em terminal.

O robô real, na classe Robot, implementou as mesmas funções do robô de teste, sem a necessidade de alterar o código de jogo.py para chamar as funções correspondentes ao robô real.

O script Untitled-1.py foi uma rotina de testes no robô para validar se todas as coordenadas de posições e ações de pegar e soltar ficha estavam corretas.

