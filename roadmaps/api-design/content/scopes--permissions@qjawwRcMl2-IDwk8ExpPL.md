# Escopos e Permissões

Escopos são rótulos anexados a uma chave de API ou token de acesso que declaram quais ações ele é permitido realizar. Em vez de uma única chave all-or-nothing, os escopos permitem emitir credenciais com acesso granular. Por exemplo, uma chave com orders:read pode buscar pedidos, mas não criar ou deletar. Isso segue o princípio da menor privilégio e limita a área de impacto se uma chave for vazada. Os escopos são um conceito fundamental no OAuth 2.0 e são igualmente aplicáveis aos sistemas simples de chave de API.

Acesse os seguintes recursos para saber mais:

- [@article@O que são Escopos de API REST?](https://auth0.com/blog/permissions-privileges-and-scopes/)
