# Caching Dependencies

Caching dependencies em GitHub Actions armazena arquivos como diretórios de gerenciadores de pacotes entre execuções de fluxo de trabalho, evitando a necessidade de reinstalar tudo do zero sempre. A ação `actions/cache` salva e restaura esses arquivos com base em uma chave, geralmente derivada do hash de um arquivo de bloqueio. Isso acelera significativamente os fluxos de trabalho que instalam as mesmas dependências repetidamente em várias execuções.

Acesse os seguintes recursos para saber mais:

- [@official@Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)
- [@video@Cache Management with GitHub actions](https://www.youtube.com/watch?v=7PVUjRXUY0o)
