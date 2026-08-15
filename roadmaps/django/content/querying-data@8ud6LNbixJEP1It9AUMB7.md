# Consultando Dados com o ORM do Django

O ORM (Object-Relational Mapper) do Django oferece uma maneira poderosa e conveniente de interagir com seu banco de dados. Em vez de escrever consultas SQL brutas, você usa código Python para recuperar dados de seus modelos. Isso envolve usar métodos como `filter()`, `get()`, `all()` e `exclude()` no gerenciador do modelo (geralmente `objects`) para especificar as condições dos dados que deseja recuperar. Esses métodos retornam QuerySets, que são coleções de instâncias de modelos lazily avaliadas que correspondem às suas critérios.

Acesse os seguintes recursos para saber mais:

- [@official@Fazendo Consultas](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-objects)
- [@article@Introdução ao ORM do Django](https://opensource.com/article/17/11/django-orm)
- [@video@Séries de Aprendizado sobre o ORM do Django](https://www.youtube.com/playlist?list=PLOLrQ9Pn6cazjoDEnwzcdWWf4SNS0QZml)
