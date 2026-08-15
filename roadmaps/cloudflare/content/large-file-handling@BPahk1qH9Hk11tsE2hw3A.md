# Manipulação de Arquivos Grandes

Manipular arquivos grandes na Cloudflare requer estratégias para evitar ultrapassar limites de tamanho e garantir a entrega eficiente. Técnicas incluem:

- **Streaming:** Processamento de arquivos em partes para reduzir o uso de memória.
- **Requisições de Intervalo:** Servindo apenas a parte solicitada de um arquivo.
- **Cloudflare Stream:** Uso do serviço de streaming de vídeo da Cloudflare para arquivos de vídeo grandes.
- **Integração com R2:** Armazenamento de arquivos grandes em R2 e serviço deles via Workers.

Esses métodos permitem lidar efetivamente com arquivos grandes, aproveitando a rede global da Cloudflare.

Acesse os seguintes recursos para saber mais:

- [@oficial@Uploads Interrompíveis e Arquivos Grandes · Cloudflare Stream](https://developers.cloudflare.com/stream/uploading-videos/resumable-uploads/)
- [@oficial@Limites do R2](https://developers.cloudflare.com/r2/platform/limits/)
