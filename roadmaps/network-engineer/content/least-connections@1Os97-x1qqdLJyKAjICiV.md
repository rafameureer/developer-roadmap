# Menos Conexões

O Algoritmo de Menos Conexões é um método de balanceamento de carga que roteia cada nova solicitação para o servidor com o menor número de conexões ativas no momento. Este abordagem é mais adaptativa do que Round Robin porque leva em conta as durações variadas das solicitações e a carga dos servidores. Ele é particularmente útil quando as solicitações têm tempos de processamento significativamente diferentes, garantindo que nenhum servidor único fique bloqueado enquanto os outros estão ociosos.

Acesse os seguintes recursos para saber mais:

- [@artigo@Tipos de algoritmos de balanceamento de carga](https://www.cloudflare.com/en-gb/learning/performance/types-of-load-balancing-algorithms/)
- [@vídeo@Algoritmos de Balanceamento de Carga LTM: Tipos de Menos Conexões](https://www.youtube.com/watch?v=tAAmZ3bz8AA)
