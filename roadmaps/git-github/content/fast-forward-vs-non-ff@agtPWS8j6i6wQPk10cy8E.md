# Fast-Forward vs Non-FF

Um merge de fast-forward acontece quando a branch-alvo não tem novos commits desde que a branch-feature foi criada, então o Git simplesmente move o ponteiro da branch para frente sem criar um novo commit. Um merge não-fast-forward ocorre quando ambas as branches divergiram, exigindo que o Git crie um commit de merge dedicado que une as duas histórias. Os desenvolvedores podem forçar um commit de merge mesmo quando um fast-forward é possível usando `git merge --no-ff`, que algumas equipes preferem para uma história mais clara.

Acesse os seguintes recursos para saber mais:

- [@artigo@Git Fast-Forward VS Non-Fast-Forward](https://leimao.github.io/blog/Git-Fast-Forward-VS-Non-Fast-Forward/)
- [@artigo@Diferença entre um git fast forward e não-fast forward](https://gist.github.com/moraisaugusto/1fa02c49b6d9833fcdf665505595ac2e)
- [@vídeo@GIT Fast Forward Visualizado](https://youtu.be/DN1fNYoJgDw?si=_TZKACj4SCOuESGm)
- [@vídeo@git merge no fast forward](https://youtu.be/X_8atqzsO8U?si=e9hMQg_aWLRMWf4O)
