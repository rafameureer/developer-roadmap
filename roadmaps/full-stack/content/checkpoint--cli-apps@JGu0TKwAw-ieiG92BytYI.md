# Checkpoint

Neste ponto, você deve ser capaz de construir aplicativos CLI usando Node.js ou qualquer linguagem de programação backend que escolheu.

Você deve ser capaz de construir um aplicativo CLI que possa:

*   Ler e escrever arquivos
*   Analisar argumentos da linha de comando
*   Fazer solicitações HTTP
*   Analisar JSON
*   Usar uma biblioteca de terceiros (por exemplo, uma biblioteca para analisar arquivos CSV)
*   Usar uma API de terceiros

Aqui estão algumas ideias para aplicativos CLI que você pode construir:

*   Crie um aplicativo CLI que aceite argumentos URL e seletor CSS e imprima o conteúdo de texto do elemento que corresponde ao seletor. **Dica**: você pode usar [cheerio](https://github.com/cheeriojs/cheerio)
*   Um aplicativo opcionalmente que aceita duas datas e imprime os projetos GitHub mais estrelados nesse intervalo de datas. **Dica**: você pode usar a [API de busca do GitHub](https://developer.github.com/v3/search/#search-repositories)
*   Renomear em massa arquivos em um diretório. **Dica**: você pode usar [fs](https://nodejs.org/api/fs.html) e [path](https://nodejs.org/api/path.html)
*   Escreva um aplicativo CLI que aceite um caminho como entrada e compacte todas as imagens nesse diretório. Ele deve aceitar uma opção para o caminho de saída; se o caminho de saída não for fornecido, ele deve compactar as imagens no local, caso contrário, escreva as imagens compactadas no caminho de saída. **Dica**: você pode usar [sharp](https://github.com/lovell/sharp).
