# Tratamento de Erros

C não possui um mecanismo de exceção embutido como alguns outros idiomas, então o tratamento de erros depende de convenções como verificar valores de retorno, definir a variável global `errno` e em algumas situações usar a terminação do programa através de códigos de saída. Isso coloca mais responsabilidade no programador para verificar e responder consistentemente às condições de falha. Pulos não-locais com `setjmp`/`longjmp` fornecem uma alternativa limitada para lidar com certos cenários de erro que precisam desfazer várias chamadas de função simultaneamente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Tratamento de Erros em C](https://www.w3schools.com/c/c_error_handling.php)
- [@artigo@As diferentes maneiras de lidar com erros em C](https://mccue.dev/pages/7-27-22-c-errors)
- [@vídeo@Tratamento de Erros | Tutorial de Programação em C](https://www.youtube.com/watch?v=OOuZLI5ingc)
