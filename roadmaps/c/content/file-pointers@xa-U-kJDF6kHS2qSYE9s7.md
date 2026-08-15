# Ponteiros de Arquivo

Um ponteiro de arquivo, do tipo `FILE *`, é retornado pela função `fopen` e representa um arquivo aberto junto com sua posição atual de leitura/gravação e estado de bufferização. Ele é passado para funções de entrada/saída subsequentes como `fread`, `fwrite` e `fclose` para identificar qual arquivo aberto eles devem operar. Cada ponteiro de arquivo aberto com sucesso deve eventualmente ser fechado com `fclose` para esvaziar qualquer dados em buffer e liberar o recurso subjacente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Arquivos em C](https://www.w3schools.com/c/c_files.php)
- [@vídeo@Básicos de Acesso a Arquivos | Tutorial de Programação em C](https://www.youtube.com/watch?v=HQNsriyMhtY)
