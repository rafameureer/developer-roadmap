# CCD

**CCD (Detecção Contínua de Colisão)** é uma técnica sofisticada usada para detectar colisões em jogos, mais avançada do que a detecção discreta tradicional. Em vez de verificar colisões em intervalos de tempo designados, CCD verifica quaisquer possíveis colisões que possam ocorrer durante todo o período ou caminho de movimento do objeto em movimento. Isso pode prevenir casos de "tunelamento", onde um objeto se move tão rápido que passa por paredes ou obstáculos sem ser detectado pela detecção discreta de colisão, devido a estar em diferentes pontos em um quadro para outro. Embora mais pesada computacionalmente do que a detecção discreta, CCD ofereça uma maior precisão na detecção de colisões, tornando-se vital em jogos onde movimentos precisos são necessários.

Acesse os seguintes recursos para saber mais:

- [@artigo@Detecção Contínua de Colisão](https://docs.unity3d.com/Manual/ContinuousCollisionDetection.html)
