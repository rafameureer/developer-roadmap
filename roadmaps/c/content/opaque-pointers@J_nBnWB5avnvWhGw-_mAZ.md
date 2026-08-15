# Ponteiros Opacos

Um ponteiro opaco é um ponteiro para uma estrutura cuja definição completa é oculta do código que o usa, geralmente declarando apenas a existência da estrutura em um arquivo de cabeçalho sem listar seus membros. Isso permite que uma biblioteca expome funções que operam no tipo enquanto mantém seus campos internos inacessíveis e livres para serem alterados, alcançando um tipo de encapsulamento semelhante aos membros privados em linguagens orientadas a objetos. Código usando um ponteiro opaco pode interagir apenas com os dados subjacentes através das funções fornecidas pela biblioteca.

Acesse os seguintes recursos para saber mais:

- [@artigo@Práticas de Design Práticas: Ponteiros Opacos e Objetos em C](https://interrupt.memfault.com/blog/opaque-pointers)
- [@artigo@Ponteiros de Dados Opacos](https://blog.aaronballman.com/2011/07/opaque-data-pointers/)
- [@vídeo@Torne seu Tipo de Dado Mais Abstrato com Tipos Opacos em C](https://www.youtube.com/watch?v=TsUOhPsZk6k)
