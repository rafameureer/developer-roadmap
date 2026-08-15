# Início frio e limitações

O início frio do AWS Lambda se refere ao atraso experimentado quando o Lambda invoca uma função pela primeira vez ou após atualizar seu código ou dependências. Isso acontece porque o Lambda precisa realizar algumas configurações iniciais, como inicializar o tempo de execução, antes de poder executar o código da função. Esse processo de configuração adiciona ao tempo de execução da função e é particularmente perceptível em situações onde a latência baixa é crítica. Os tempos de início frio também variam com base no tamanho da memória, com funções lambda maiores levando mais tempo para iniciar. Além disso, funções não utilizadas podem enfrentar um novo início frio conforme AWS pode limpar recursos ociosos em determinados momentos.

Acesse os seguintes recursos para saber mais:

- [@oficial@Início frio e limitações do Lambda](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
