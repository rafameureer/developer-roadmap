# Tratamento de Solicitações/Respostas

Os Trabalhadores do Cloudflare são excelentes em interceptar e modificar solicitações e respostas HTTP. Quando uma solicitação atinge o Cloudflare, um Trabalhador pode inspecionar os detalhes da solicitação (cabeçalhos, URL, método) e tomar ações: reescrever a URL, modificar cabeçalhos ou até mesmo servir uma resposta completamente diferente. Da mesma forma, os Trabalhadores podem interceptar respostas do servidor de origem, modificando o conteúdo, adicionando cabeçalhos para cache ou até mesmo servindo uma versão em cache diretamente. Esse nível de controle permite a personalização e otimização poderosas do tráfego web.

Acesse os seguintes recursos para saber mais:

- [@oficial@Solicitação e Resposta](https://developers.cloudflare.com/workers/runtime-apis/request)
- [@artigo@API Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
