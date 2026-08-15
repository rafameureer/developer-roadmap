# Uso de Ferramentas pelo Anthropic

O Uso de Ferramentas pelo Anthropic permite conectar um modelo Claude a funções reais de software, permitindo que o agente execute tarefas úteis por conta própria. Você fornece ao Claude uma lista de ferramentas, cada uma com um nome, uma curta descrição e um esquema JSON estrito que mostra os campos de entrada permitidos. Durante uma conversa, você envia texto do usuário mais essa lista de ferramentas. O Claude decide se uma ferramenta deve ser executada, escolhe uma e retorna um bloco JSON que corresponde ao esquema. Seu código lê o JSON, chama a função correspondente e envia o resultado de volta para o Claude para a próxima etapa. Esse loop repete até que não seja mais necessário fazer chamadas de ferramenta. Esquemas claros, conjuntos de campos pequenos e exemplos úteis tornam as chamadas precisas. Ao manter o modelo responsável por escolher as ferramentas enquanto seu código controla ações reais, você ganha flexibilidade e segurança.

Acesse os seguintes recursos para saber mais:

- [@official@Uso de Ferramentas pelo Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
