# DBVT

`DBVT` ou `Dynamic Bounding Volume Tree` é uma estrutura de dados de aceleração que é principalmente usada em simulações físicas como detecção de colisão. É um tipo de BVH (`Bounding Volume Hierarchy`), mas a característica única do DBVT é seu tratamento de objetos dinâmicos. Como o nome sugere, ele foi especificamente projetado para lidar eficientemente com cenários em mudança, como objetos se movendo ou ambientes evoluindo, melhor que um BVH típico. Diferentemente de um BVH estático, o DBVT atualiza dinamicamente a árvore conforme os objetos se movem, mantendo a eficiência das consultas de colisão. Ele faz isso principalmente através da rotação da árvore e ajuste dos volumes delimitadores em vez de reconstruir completamente a árvore. Isso torna o DBVT uma opção altamente atraente para cenários com dinâmica significativa.

Acesse os seguintes recursos para saber mais:

- [@artigo@DBVT](https://sopiro.github.io/DynamicBVH/)
- [@artigo@Hierarquias de Volume Delimitador Dinâmicas](https://box2d.org/files/ErinCatto_DynamicBVH_Full.pdf)
