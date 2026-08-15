# Leituras e Escritas Retransmissíveis

Leituras e escritas retransmissíveis no MongoDB são recursos do lado do cliente que automaticamente repetem determinadas operações de banco de dados quando elas encrontram erros de rede transitórios ou indisponibilidade temporária do servidor, melhorando a resiliência da aplicação e a experiência do usuário. Os drivers do MongoDB podem retransmitir automaticamente operações de leitura e certas operações de escrita (como inserções, atualizações, exclusões e findAndModify) exatamente uma vez quando elas falham devido a problemas de rede, eleições de conjunto de réplicas ou outros erros recuperáveis, sem exigir alterações no código da aplicação. Esta funcionalidade é particularmente valiosa em ambientes distribuídos, implantações na nuvem e configurações de conjunto de réplicas onde problemas temporários de conectividade ou eventos de failover são comuns, pois reduz a probabilidade de erros de aplicativo e fornece uma melhor experiência do usuário lidando com falhas transitórias transparentemente.

Acesse os seguintes recursos para saber mais:

- [@oficial@Leituras Retransmissíveis](https://www.mongodb.com/docs/manual/core/retryable-writes/)
- [@oficial@Escritas Retransmissíveis](https://www.mongodb.com/docs/manual/core/retryable-reads/)
