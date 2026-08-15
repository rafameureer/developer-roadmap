# Limitação de Taxa

O Cloudflare Queues pode ser usado para implementar limitação de taxa. Em vez de processar diretamente todas as solicitações, você pode enfileirá-las. Um Worker consumidor então processa mensagens da fila em um ritmo controlado. Isso previne que seus sistemas de back-end sejam sobrecarregados por picos repentinos de tráfego. Você pode ajustar a taxa de processamento do consumidor para corresponder à capacidade dos seus serviços de back-end.

Acesse os seguintes recursos para saber mais:

- [@oficial@Cloudflare Queues - Filas e Limitação de Taxa](https://developers.cloudflare.com/queues/tutorials/handle-rate-limits/)
- [@oficial@Melhores Práticas de Limitação de Taxa - Documentação do Cloudflare](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/)
