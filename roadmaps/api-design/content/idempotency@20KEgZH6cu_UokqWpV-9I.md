# Idempotência na Design de APIs

Idempotência na design de APIs refere-se ao conceito onde múltiplas solicitações idênticas têm o mesmo efeito que uma única solicitação. Isso significa que, independentemente do número de vezes que um cliente envia a mesma solicitação para o servidor, o estado do servidor permanece o mesmo após a primeira solicitação. Designar APIs como idempotentes é essencial para a confiabilidade, pois permite reações sem efeitos colaterais, reduz complexidade em sistemas distribuídos e fornece uma melhor experiência de usuário em condições de rede instáveis. Entender conceitos de idempotência pode aumentar a robustez e tolerância a falhas das suas APIs. Geralmente é aplicável aos métodos `PUT`, `DELETE` e às vezes ao método `POST` em APIs RESTful.

Acesse os seguintes recursos para saber mais:

- [@artigo@O que é idempotência?](https://blog.dreamfactory.com/what-is-idempotency)
- [@artigo@Idempotência é fácil até a segunda solicitação ser diferente](https://blog.dochia.dev/blog/idempotency/)
- [@artigo@Api REST Idempotente](https://restfulapi.net/idempotent-rest-apis/)
