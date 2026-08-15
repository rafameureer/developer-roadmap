# Filtros de Registro

Os filtros no framework de registro do Django fornecem uma maneira de adicionar controle extra sobre quais registros de log são processados por um manipulador. Eles determinam se um registro de log específico deve ser emitido com base em critérios que você define. Isso permite incluir ou excluir mensagens de log selecionadamente com base em atributos como o nome do registrador, nível de log ou qualquer outra lógica personalizada que você implementar. Os filtros são anexados a manipuladores e um manipulador só processará um registro de log se todos os seus filtros permitirem.

Acesse os seguintes recursos para saber mais:

- [@oficial@Filtros](https://docs.djangoproject.com/pt-br/6.0/topics/logging/#topic-logging-parts-filters)
- [@artigo@Registro no Django — Parte II [Filtros e Formatters]](https://medium.com/django-unleashed/logging-in-django-part-ii-filters-and-formatters-c7190d360ab2)
