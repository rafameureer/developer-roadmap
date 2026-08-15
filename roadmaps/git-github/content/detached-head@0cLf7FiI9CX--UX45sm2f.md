# Detached HEAD

O estado de HEAD desanexado ocorre quando o HEAD aponta diretamente para um commit específico em vez de uma branch, geralmente após verificar out a hash do commit ou a tag. Qualquer novo commit feito nesse estado não está anexado a uma branch, então pode ser perdido uma vez que outra branch for verificada, a menos que uma nova branch seja criada para salvá-los. Esse estado é frequentemente usado para inspecionar commits antigos sem afetar a branch atual.

Acesse os seguintes recursos para saber mais:

- [@artigo@Como resolver o estado de HEAD desanexado no Git](https://graphite.dev/guides/how-to-resolve-detached-head-state-in-git)
- [@vídeo@HEAD & Detached Head](https://www.youtube.com/watch?v=HvDjbAa9ZsY)
