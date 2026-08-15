# Tracert

O Tracert, abreviação de traceroute, é uma ferramenta de utilidade em linha de comando usada para rastrear o caminho que os pacotes percorrem para atingir um destino específico. Ele funciona enviando pacotes com valores TTL (Time-To-Live) incrementais. À medida que cada roteador ao longo do caminho recebe um pacote, ele decrementa o TTL. Quando o TTL chega a zero, o roteador envia de volta uma mensagem ICMP "Tempo Excedido" para a fonte. Analisando essas mensagens, o Tracert identifica cada roteador (hop) no caminho e mede o tempo de ida-volta (RTT) para cada hop.

Acesse os seguintes recursos para saber mais:

- [@article@Manual Page do traceroute](https://linux.die.net/man/8/traceroute)
- [@article@Tracert](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert)
- [@video@Tracert (tracert) Explained](https://www.youtube.com/watch?v=up3bcBLZS74)
