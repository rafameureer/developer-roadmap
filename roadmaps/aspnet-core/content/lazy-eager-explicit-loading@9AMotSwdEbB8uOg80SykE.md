# Carregamento Eager, Lazy e Explícito

Carregamento Eager
-----------------

O Carregamento Eager ajuda você a carregar todas as entidades necessárias de uma só vez; ou seja, todas as suas entidades filhas serão carregadas em uma única chamada ao banco de dados. Isso pode ser alcançado usando o método Include, que retorna as entidades relacionadas como parte da consulta e muitos dados são carregados de uma só vez.

Carregamento Lazy
----------------

É o comportamento padrão do Entity Framework, onde uma entidade filha é carregada apenas quando ela é acessada pela primeira vez. Ele simplesmente adia a carga dos dados relacionados até que você solicite isso.

Acesse os seguintes recursos para saber mais:

- [@article@Carregamento Eager e Carregamento Lazy](https://www.c-sharpcorner.com/article/eager-loading-lazy-loading-and-explicit-loading-in-entity-framework/)
- [@article@Diferença entre Carregamento Eager e Carregamento Lazy](https://stackoverflow.com/questions/31366236/lazy-loading-vs-eager-loading)
- [@article@Trabalhando com Carregamento Eager e Carregamento Lazy no Entity Framework](https://dzone.com/articles/working-with-lazy-loading-and-eager-loading-in-ent)
