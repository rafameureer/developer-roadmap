# OBB

`Oriented Bounding Box (OBB)` é um tipo de volume delimitador usado em gráficos computacionais e geometria computacional. Ele é frequentemente usado para simplificar objetos geométricos complexos correlacionando-os como uma caixa muito mais próxima em tamanho e orientação ao objeto real. Diferentemente da `Axis-Aligned Bounding Box (AABB)`, o `OBB` não está limitado a alinhar com os eixos, então a caixa pode ser rotacionada. Esta orientação geralmente é escolhida com base no sistema de coordenadas locais do objeto, então o `OBB` mantém sua rotação. As propriedades de um `OBB` incluem seu centro, dimensões e orientação. No entanto, vale ressaltar que os `OBBs` podem ser mais intensos em termos computacionais do que os `AABBs` devido à complexidade matemática.

Acesse os seguintes recursos para saber mais:

- [@artigo@Comparação entre OBB e OBB](https://gamedev.stackexchange.com/questions/25397/obb-vs-obb-collision-detection)
- [@artigo@Oriented Bounding Box](https://gamedev.stackexchange.com/questions/49041/oriented-bounding-box-how-to)
