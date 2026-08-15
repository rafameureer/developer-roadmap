# Camadas

As camadas do AWS Lambda são mecanismos de distribuição para bibliotecas, tempo de execução personalizado e outras dependências de funções. Em outras palavras, são um mecanismo de distribuição para artefatos. As camadas podem ser versificadas, e cada versão é imutável. Uma camada do AWS Lambda é um arquivo ZIP que contém bibliotecas, um tempo de execução personalizado ou outras dependências. Funções Lambda podem ser configuradas para fazer referência a essas camadas. A camada é então extraída para o diretório `/opt` no ambiente de execução da função. Cada tempo de execução procura por bibliotecas em uma localização diferente sob o diretório `/opt`, dependendo da linguagem.

Acesse os seguintes recursos para saber mais:

- [@oficial@Camadas do AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html)
- [@vídeo@Criar e Usar Camadas do Lambda](https://www.youtube.com/watch?v=jyuZDkiHe2Q)
