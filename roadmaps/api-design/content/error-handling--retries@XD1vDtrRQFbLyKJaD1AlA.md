# Tratamento de Erros / Tentativas

Ao criar designs de API eficazes, abordar o Tratamento de Erros e as Tentativas é um aspecto essencial. Isso ocorre porque as APIs não são sempre livres de erros e podem haver casos de interrupções temporárias da rede ou inacurácias de entrada dos usuários. Sem uma tratativa robusta de erros, tais ocorrências podem levar facilmente a falhas catastróficas na aplicação ou experiências de usuário insatisfatórias. O tratamento de erros pode envolver validar entradas, gerenciar exceções e retornar mensagens de erro ou códigos de status apropriados para o usuário. Enquanto isso, o conceito de tentativas entra em jogo para garantir a máxima taxa de sucesso das solicitações em meio a falhas transitórias. Com a implementação correta de tentativas, uma API pode repetidamente tentar executar uma solicitação até que ela seja bem-sucedida, assim assegurando uma operação suave.

Acesse os seguintes recursos para saber mais:

- [@artigo@Como melhorar seu backend adicionando tentativas às chamadas de API](https://hackernoon.com/how-to-improve-your-backend-by-adding-retries-to-your-api-calls-83r3udx)
- [@vídeo@Como criar aplicativos web resilientes com tentativas](https://www.youtube.com/watch?v=Gly94hp3Eec)
