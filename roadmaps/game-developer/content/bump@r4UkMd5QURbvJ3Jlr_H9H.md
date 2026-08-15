# Bump

`Bump` é muito semelhante a texturas. Na verdade, é um tipo de textura em si. Se você pegar a textura de uma parede revestida com tijolos, vai se perceber gradualmente que a quantidade de detalhes presentes dentro da parede, se processados geometricamente, seria extremamente exigente e desperdiçoso. Para combater essa ineficiência, foram criadas as `bump maps`. Tradicionalmente, uma textura plana seria apenas uma imagem de algo chamado de `mapa de cor`, ou seja, onde cada cor individual do pixel deve estar para representar uma textura. Quando você tira a foto da sua chão, parede ou qualquer objeto, essa imagem na essência é o mapa de cor. O bump map é diferente porque informa à textura seus valores `normal`. Então, se você pegar uma malha 2D plana e aplicar um bump map nela, ela renderizará a mesma malha 2D com todos os valores normais incorporados na malha 2D plana, criando um efeito gráfico que simula a dimensionalidade tridimensional.

Acesse os seguintes recursos para saber mais:

- [@artigo@Bump Maps](https://developer.valvesoftware.com/wiki/Bump_map)
- [@vídeo@Normais, Mapas Normais e Bump Maps](https://www.youtube.com/watch?v=l5PYyzsZED8)
- [@vídeo@Bump, Normal e Deslocamento](https://www.youtube.com/watch?v=43Ilra6fNGc)
