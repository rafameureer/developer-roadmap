# git push --force

`git push --force` sobrescreve o histórico da branch remota com o histórico da branch local, mesmo que eles tenham divergido. Isso é necessário após reescrever os commits locais, como através de um rebase, já que um push normal seria rejeitado devido a um histórico desencaixado. Porque ele pode sobrescrever o trabalho dos outros em uma branch compartilhada, `git push --force-with-lease` é geralmente recomendado em vez disso, pois falha se a branch remota tiver alterações que a branch local não esteja ciente.

Acesse os seguintes recursos para saber mais:

- [@artigo@Git Push Force](https://www.gitkraken.com/learn/git/problems/git-push-force)
- [@vídeo@Como forçar um push no GitHub?](https://www.youtube.com/watch?v=wgXbfLn-zkI)
