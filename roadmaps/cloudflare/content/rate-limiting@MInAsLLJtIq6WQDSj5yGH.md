# Limitação de Taxa

As Filas do Cloudflare podem ser usadas para implementar a limitação de taxa. Em vez de processar diretamente todas as solicitações, você pode enfileirá-las. Um Trabalhador Consumidor então processará mensagens da fila em um ritmo controlado. Isso previne que seus sistemas de back-end sejam sobrecarregados por picos repentinos no tráfego. Você pode ajustar a taxa de processamento do consumidor para corresponder à capacidade dos seus serviços de back-end.

Acesse os seguintes recursos para saber mais:

- [@oficial@Filas do Cloudflare - Filas e Limitações de Taxa](https://developers.cloudflare.com/queues/tutorials/handle-rate-limits/)
- [@oficial@Melhores Práticas de Limitação de Taxa - Documentação do Cloudflare](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/)
