# Leitura e Escrita de Arquivos

Leitura e escrita de arquivos em C usa funções como `fread` e `fwrite` para dados binários, ou `fgets`, `fputs`, e `fprintf` para texto, todos operando em um `FILE *` obtido por meio de `fopen`. Cada função precisa ser verificada quanto à quantidade de dados que ela realmente transferiu, pois leituras e escritas podem retornar menos do solicitado, por exemplo, no final de um arquivo. Verificar adequadamente esses valores de retorno captura erros que, caso contrário, produziriam silenciosamente dados incompletos ou corrompidos.
