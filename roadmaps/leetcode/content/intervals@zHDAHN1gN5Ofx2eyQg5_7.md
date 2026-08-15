# Intervalos

Problemas de intervalo aparecem com frequência em problemas de agendamento, calendário e perguntas baseadas em intervalos. A técnica dominante é ordenar por tempo de início ou fim, o que transforma um problema de verificação de sobreposição quadrático em uma varredura linear. Uma vez ordenados, você pode mesclar sobreposições, contar eventos simultâneos ou encontrar lacunas com uma única passagem. Os problemas mais difíceis nesta fase combinam a ordenação de intervalos com uma heap para responder às consultas eficientemente. A mudança de mindset chave é pensar em intervalos como objetos com início e fim, e raciocinar sobre o que significa que dois intervalos se sobrepõem, contenham ou estejam adjacentes.

Acesse os seguintes recursos para saber mais:

- [@artigo@Fundamentos da DSA: Intervalos - De Teoria a Prática no LeetCode](https://www.jaykye.dev/blog/dsa-intervals-fundamentals)
