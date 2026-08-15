# Sombra de Stencil

As `sombras de stencil` são uma técnica utilizada em gráficos computacionais 3D para criar sombras. O algoritmo de sombra de stencil opera tratando a sombra como um volume tridimensional de espaço, conhecido como volume de sombra. Qualquer parte da cena que esteja dentro deste volume de sombra estará em sombra. Se estiver fora do volume de sombra, estará na luz. O volume de sombra é criado extrudando a silhueta poligonal de um objeto 3D no espaço pelas linhas de visão da fonte de luz. Para objetos complexos equivalentes, o número de arestas ou vértices para preencher o buffer de stencil geralmente será menor que o número de pixels necessários para calcular mapas de sombra, tornando as sombras de stencil mais eficientes nesse aspecto. No entanto, as sombras produzidas por essa técnica podem parecer bloqueadas ou realistas se não forem refinadas adicionalmente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Implementação de Sombras de Stencil](https://devforum.roblox.com/t/stencil-shadows-implementation/2079287)
