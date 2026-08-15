# Tracert

O Tracert (traceroute) é uma ferramenta de diagnóstico de rede em linha de comando usada para rastrear o caminho que um pacote percorre de seu computador até um destino especificado. Ele funciona enviando uma série de pacotes com valores increasing time-to-live (TTL). Cada roteador ao longo do caminho decrementa o TTL, e quando o TTL de um pacote chega a zero, o roteador envia de volta uma mensagem ICMP "tempo excedido". O Tracert registra essas respostas de cada roteador, fornecendo uma lista de hops e o tempo de ida-volta para cada hop.

Acesse os seguintes recursos para saber mais:

- [@article@Manual Page do traceroute](https://linux.die.net/man/8/traceroute)
- [@article@Tracert](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert)
- [@video@Tracert (tracert) Explained](https://www.youtube.com/watch?v=up3bcBLZS74)
