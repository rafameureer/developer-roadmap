# Expirando

Índices expirados (TTL - Time To Live) no MongoDB automaticamente excluem documentos de uma coleção após um período especificado, tornando-os ideais para gerenciar dados sensíveis ao tempo como informações de sessão, entradas de log, caches temporários ou qualquer dado que se torna obsoleto após um determinado período. Esses índices são criados em campos de data e usam um processo em segundo plano que roda a cada 60 segundos para remover documentos expirados, ajudando a manter o tamanho ótimo da coleção e desempenho ao evitar a acumulação de dados obsoletos. Índices TTL são particularmente úteis para aplicativos que geram grandes volumes de dados transientes, pois fornecem um mecanismo de limpeza automática que reduz custos de armazenamento e melhora o desempenho das consultas sem a necessidade de intervenção manual ou lógica complexa do aplicativo para lidar com a expiração dos dados.

Acesse os seguintes recursos para saber mais:

- [@official@Excluir Dados de Coleções Definindo TTL](https://www.mongodb.com/docs/manual/tutorial/expire-data/)
- [@article@Entendendo TTL no MongoDB](https://medium.com/@darshitanjaria/understanding-ttl-in-mongodb-automatically-expiring-documents-e8b1defc1158)
- [@article@Compreendendo Índices e Expiração do MongoDB](https://stenzr.medium.com/understanding-mongodb-indexes-and-expiry-019831790542)
