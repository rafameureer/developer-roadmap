# Ligação de Dados

A ligação de dados do SwiftUI é um mecanismo que cria uma conexão bidirecional entre um pedaço de dados e um elemento da interface do usuário. Ele usa o wrapper de propriedade `@Binding` para permitir que as exibições filhas compartilhem e modifiquem dados proprietários das exibições pai. As vinculações garantem que alterações em dados sejam refletidas imediatamente na interface do usuário e vice-versa. Eles são geralmente criados usando o prefixo `$` em uma propriedade `@State`. Este abordagem facilita a circulação de dados através da hierarquia de exibições de um aplicativo, permitindo atualizações reativas da interface do usuário e mantendo uma única fonte de verdade.

Acesse os seguintes recursos para saber mais:

- [@oficial@Ligação](https://developer.apple.com/documentation/swiftui/binding)
- [@oficial@Tutoriais da Apple: Passando dados com vinculações](https://developer.apple.com/tutorials/app-dev-training/passing-data-with-bindings)
- [@vídeo@Como usar o wrapper de propriedade @Binding no SwiftUI](https://www.youtube.com/watch?v=btDMzB5x2Gs)
- [@vídeo@SwiftUI - Explicação do Wrapper de Propriedade @Binding](https://www.youtube.com/watch?v=lgtB3WLEOYg)
