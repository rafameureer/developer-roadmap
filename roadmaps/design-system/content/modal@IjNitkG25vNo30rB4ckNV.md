# Modal

Modais são contêineres que aparecem na frente do conteúdo principal para fornecer informações críticas ou um pedaço de conteúdo ação.

- **Suporta qualquer tipo de Conteúdo:** Como qualquer outro contêiner, modais podem ser usados em diferentes cenários e você deve ser capaz de usá-lo com qualquer outro componente dentro.
- **Ações Suplementares:** Como o conteúdo do modal pode ser açãoável, é importante ter uma área para elementos de ação. Essa área geralmente está localizada no fundo do contêiner do modal.
- **Ação Fechar:** Os modais devem fornecer uma maneira clara de fechamento, pois estão bloqueando o conteúdo quando abertos. Isso pode ser um botão de fechamento separado ou uma das ações suplementares.
- **Estrutura de Informações:** Mesmo que os modais possam ser usados como um contêiner vazio para o conteúdo, eles precisam de uma estrutura de informações definida para fornecer uma experiência holística. Isso pode incluir definir como títulos e subtítulos aparecem por padrão ou onde a área de um elemento de ação está localizada.
- **Suporte à Navegação com Teclado:** Deve ser possível fechar um modal pressionando a tecla Esc e todos os elementos focáveis dentro do contêiner do modal devem ser acessíveis com a navegação por teclado.
- **Trapping de Foco:** Uma vez que um modal é aberto, o foco deve ser movido para o primeiro elemento dentro do modal e deve ser loopado dentro do contêiner do modal. Fechar o modal deve retornar o foco ao último elemento focado na página.
