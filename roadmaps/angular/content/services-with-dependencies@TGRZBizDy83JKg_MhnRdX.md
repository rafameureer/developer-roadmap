# Testando serviços com dependências

Quando você adiciona uma dependência ao seu serviço, também deve incluí-la em seus testes. Para testes isolados, passe uma instância da classe de dependência injetável para o construtor do serviço. Usar a função `inject` pode adicionar complexidade. Injetar o serviço real é geralmente impraticável porque serviços dependentes podem ser difíceis de criar e controlar. Em vez disso, simule a dependência, use um valor falso ou crie um espia na método do serviço relevante. Usando a utilidade de teste `TestBed`, você pode deixar que a injeção de dependências do Angular lidem com a criação do serviço e o gerenciamento da ordem dos argumentos do construtor.

Acesse os seguintes recursos para saber mais:

- [@oficial@Testando Serviços](https://angular.dev/guide/testing/services)
- [@artigo@Testing-Angular.com](https://testing-angular.com/testing-services/)
- [@vídeo@Testando o Serviço que tem outro serviço injetado através da Injeção de Dependência](https://www.youtube.com/watch?v=ACb8wqwgOV4)
- [@vídeo@Testando Serviços que têm HttpClient como dependência usando Jasmine Spy](https://www.youtube.com/watch?v=15othucRXcI)
- [@vídeo@Angular Unit Tests com a função inject()](https://www.youtube.com/watch?v=Tvsa4OMUGXs)
