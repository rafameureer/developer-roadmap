# Clipping

`Clipping` é uma técnica fundamental em gráficos computacionais, principalmente usada para renderizar eficientemente um cenário tridimensional. Esse processo envolve eliminar certas partes de objetos no cenário que estão fora da visão ou bloqueadas por outros objetos. O clipping pode ocorrer de várias maneiras, uma das métodos mais comuns sendo `Culling de Frustum de Visão` onde objetos completamente fora do campo de visão da câmera são descartados. O objetivo do clipping é otimizar a pipeline de renderização gráfica reduzindo o número de polígonos que a hardware gráfica precisa processar. Consequentemente, isso ajuda a melhorar a velocidade e o desempenho geral do processo de renderização.

Acesse os seguintes recursos para saber mais:

- [@artigo@Clipping em Jogos](https://www.haroldserrano.com/blog/what-is-clipping-in-opengl)
