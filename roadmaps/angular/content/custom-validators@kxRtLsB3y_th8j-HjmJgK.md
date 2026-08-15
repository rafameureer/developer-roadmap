# Validadores Personalizados

Os validadores personalizados no Angular são funções que permitem definir sua própria lógica de validação para os controles de formulário. Eles são usados quando os validadores embutidos (como `required`, `minLength`, etc.) não atendem às suas exigências específicas de validação. Um validador personalizado é uma função que retorna `null` se o controle do formulário for válido, ou um objeto que representa o erro de validação se ele for inválido. Esse objeto geralmente contém um par chave-valor onde a chave é o nome do erro e o valor é um booleano ou alguns detalhes sobre o erro.

Visite os seguintes recursos para saber mais:

- [@official@Definindo validadores personalizados](https://angular.dev/guide/forms/form-validation#defining-custom-validators)
- [@video@Como criar um validador personalizado no Angular 17](https://youtu.be/3TwmS0Gdg9I?si=1w4EX-HifJ70-CxT)
