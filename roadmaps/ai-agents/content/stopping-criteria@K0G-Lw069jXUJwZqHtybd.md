# Critérios de Parada

Os critérios de parada informam ao modelo linguístico quando para de escrever mais texto. Sem eles, o modelo poderia continuar adicionando palavras por sempre, desperdiçar tempo ou sair do ponto em que estamos interessados. Regras comuns incluem um número máximo de tokens, um token especial de fim de sequência ou uma string personalizada como `“\n\n”`. Também podemos parar quando a resposta começar a se repetir ou atingir uma pontuação que significa que ela está fora do tópico. Boas regras de parada economizam custo, aceleram as respostas e evitam conteúdo sem sentido ou inseguro.

Acesse os seguintes recursos para saber mais:

- [@artigo@Definindo Critérios de Parada em Modelos de Linguagem Grandes](https://www.metriccoders.com/post/defining-stopping-criteria-in-large-language-models-a-practical-guide)
