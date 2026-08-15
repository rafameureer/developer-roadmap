# SAT

`SAT`, ou teorema de eixo separador, é frequentemente usado na detecção de colisões em desenvolvimento de jogos. Seu benefício principal é para a detecção rápida e simples de se dois polígonos convexos se intersectam. O teorema é um pouco complexo - funciona projetando todos os pontos de ambos os polígonos sobre vários eixos ao redor das formas, em seguida verificando por sobreposições. No entanto, pode ser relativamente demorado lidar com modelos mais complexos ou muitos objetos, pois ele precisa calcular as projeções, então geralmente é usado em um sistema de detecção de fase ampla. Uma explicação profunda de como `sat` funciona pode envolver alguns conceitos matemáticos ou auxílios visuais, mas isso é a base do seu uso no desenvolvimento de jogos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Teorema de Eixo Separador](https://dyn4j.org/2010/01/sat/)
- [@artigo@Detecção de Colisão Usando o Teorema de Eixo Separador](https://code.tutsplus.com/collision-detection-using-the-separating-axis-theorem--gamedev-169t)
