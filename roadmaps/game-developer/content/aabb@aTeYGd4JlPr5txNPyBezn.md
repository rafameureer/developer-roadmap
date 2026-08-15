# AABB

`AABB`, sigla para Axis-Aligned Bounding Box, é um formato comum de volume limitante usado no desenvolvimento de jogos. É uma caixa que se alinha diretamente com os eixos do sistema de coordenadas e envolve um objeto de jogo. Os lados de um AABB estão alinhados aos eixos, o que é útil quando se realiza determinados cálculos, já que caixas não alinhadas aos eixos exigiriam matemática mais complexa. Os AABBs são principalmente usados para a detecção de colisão de fase ampla, o que significa verificar se dois objetos podem estar em processo de colidir. Apesar dos AABBs serem relativamente conservadores e terem mais volume limitante do que caixas de volume limitante orientadas (OBBs), eles são mais simples e mais rápidos de usar na detecção de colisão.

Acesse os seguintes recursos para saber mais:

- [@artigo@Axis-Aligned Bounding Box](https://gdbooks.gitbooks.io/3dcollisions/content/Chapter1/aabb.html)
