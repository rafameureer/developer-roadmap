# Hierarquia de Volume Limitante (BVH)

BVH, ou Hierarquia de Volume Limitante, é um algoritmo usado em gráficos computacionais 3D para acelerar o processo de renderização. Ele organiza a geometria em uma estrutura hierárquica onde cada nó na árvore representa um volume limitante (um volume que envolve ou contém um ou mais objetos geométricos). O nó raiz da BVH contém todos os outros nós ou objetos geométricos, seus nós filhos representam uma partição do espaço e as folhas são geralmente objetos geométricos individuais. A principal meta de usar BVH é excluir rapidamente grandes partes da cena do processo de renderização, para reduzir a carga computacional de avaliar cada objeto individualmente na cena.

Acesse os seguintes recursos para saber mais:

- [@opensource@UnityBoundingVolumeHeirachy](https://github.com/rossborchers/UnityBoundingVolumeHeirachy)
