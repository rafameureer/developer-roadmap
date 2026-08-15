# Transações

As transações são uma maneira de agrupar uma série de operações de banco de dados em uma única unidade de trabalho. Isso significa que todas as operações dentro da transação devem ser bem-sucedidas ou nenhuma delas deve ser. Se qualquer operação falhar, o banco de dados reverterá para seu estado anterior, garantindo a consistência e integridade dos dados. Isso é especialmente útil ao realizar várias atualizações relacionadas no banco de dados, onde uma falha em uma atualização pode deixar o banco de dados em um estado inconsistente.

Acesse os seguintes recursos para saber mais:

- [@official@Transações do Banco de Dados](https://docs.djangoproject.com/pt-br/4.1/topics/db/transactions/)
- [@article@Entendendo a Atômicaidade das Transações no Django](https://plainenglish.io/blog/understanding-djangos-transaction-atomic)
- [@article@Python: Como Funcionam as Transações do Django](https://m-t-a.medium.com/python-how-django-transactions-work-a87083303102)
- [@video@Transações de Banco de Dados no Django / Função atomic()](https://www.youtube.com/watch?v=L8k8Ukw1P6U)
