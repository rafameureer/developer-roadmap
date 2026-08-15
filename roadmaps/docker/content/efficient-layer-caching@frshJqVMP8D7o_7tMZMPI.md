# Cache de Camadas Eficiente

Ao construir imagens de contêiner, o Docker armazena em cache as camadas recentemente criadas. Essas camadas podem ser usadas posteriormente ao construir outras imagens, reduzindo o tempo de construção e minimizando o uso de largura de banda. No entanto, para tirar o máximo proveito deste mecanismo de cacheamento, é necessário estar ciente de como usar eficientemente o cacheamento de camadas. O Docker cria uma nova camada para cada instrução (por exemplo, `RUN`, `COPY`, `ADD`, etc.) no Dockerfile. Se a instrução não tiver mudado desde a última construção, o Docker reutilizará a camada existente.

Acesse os seguintes recursos para saber mais:

- [@official@Cacheamento de Camadas do Docker](https://docs.docker.com/build/cache/)
- [@video@Cacheamento de Camadas](https://www.youtube.com/watch?v=_nMpndIyaBU)
