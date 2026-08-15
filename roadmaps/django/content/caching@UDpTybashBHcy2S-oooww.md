# Cache

O cache é uma técnica para armazenar dados acessados frequentemente em um local de armazenamento temporário (o cache) para acelerar a recuperação no futuro. Quando os dados são solicitados, o sistema primeiro verifica o cache. Se os dados estiverem presentes (um "acerto de cache"), eles serão servidos diretamente do cache, evitando o processo mais lento de recuperá-los da fonte original (como um banco de dados). Se os dados não estiverem no cache (um "falha de cache"), eles serão recuperados da fonte original, armazenados no cache e depois servidos ao usuário. Isso reduz a latência e melhora o desempenho da aplicação.

Acesse os seguintes recursos para saber mais:

- [@official@Quadro de Cache do Django](https://docs.djangoproject.com/pt-br/3.2/topics/cache/)
- [@article@Django Caching 101: Entendendo os Básicos e Além disso](https://dev.to/pragativerma18/django-caching-101-understanding-the-basics-and-beyond-49p)
- [@article@Exemplos de Cache no Django com um Projeto Completo](https://medium.com/django-unleashed/django-cache-examples-with-a-complete-project-7307322756e2)
- [@video@Cache com Redis e Django!](https://www.youtube.com/watch?v=5W2Yff00H8s)
