# Git Bisect

Git Bisect é uma ferramenta interativa usada para identificar qual commit na história do seu projeto introduziu um bug ou regressão. Você começa identificando dois commits: um onde o problema não está presente (o "commit bom") e outro onde ele ocorre (o "commit ruim"). Em seguida, execute `git bisect start`, seguido por `git bisect good` para o commit bom e `git bisect bad` para o commit ruim. Git Bisect guiará você através de um processo de busca binária, pedindo que teste o ponto médio do seu intervalo atual até identificar o commit exato que introduziu o bug ou regressão.

Acesse os seguintes recursos para saber mais:

- [@official@Git Bisect](https://git-scm.com/docs/git-bisect)
- [@article@Usando git bisect para encontrar o commit defeituoso](https://dev.to/alvesjessica/using-git-bisect-to-find-the-faulty-commit-25gf)
- [@video@Git Bisect | Como usar Git Bisect | Aprenda Git](https://www.youtube.com/watch?v=z-AkSXDqodc)
