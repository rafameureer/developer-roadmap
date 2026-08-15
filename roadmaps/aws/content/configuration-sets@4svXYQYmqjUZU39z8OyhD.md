# Conjuntos de Configuração

Os Conjuntos de Configuração no SES (Simple Email Service) do AWS (Amazon Web Services) permitem que você publique eventos de envio de e-mail. Esses conjuntos são usados para agrupar regras semelhantes que você pode aplicar aos e-mails que envia usando o AWS SES. Você pode aplicar um conjunto de configuração a um e-mail incluindo-o nos cabeçalhos do e-mail. Ele pode ser usado para especificar pools de IPs dedicados de envio, configurar os parâmetros de entrega da mensagem e habilitar o rastreamento de abertura e clique. O AWS SES envia informações sobre cada e-mail enviado com o conjunto para o CloudWatch e Kinesis Firehose, que podem ser usados posteriormente para análise adicional ou para gerenciar suas interações com os clientes de maneira mais eficaz.

Acesse os seguintes recursos para saber mais:

- [@oficial@SES](https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets.html)
