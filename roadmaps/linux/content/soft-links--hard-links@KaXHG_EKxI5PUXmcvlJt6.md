# Links Simbólicos (Soft) e Hards

O Linux suporta dois tipos de links de arquivo. Os links hards compartilham o mesmo inode e dados do arquivo original - se o original for excluído, os dados permanecerão acessíveis. Os links simbólicos (links simbólicos) são atalhos que apontam para o caminho do arquivo original - eles quebram se o original for removido. Crie com `ln` para links hards e `ln -s` para links simbólicos.

Visite os seguintes recursos para saber mais:

- [@article@Hard links e Soft links no Linux explicados](https://www.redhat.com/en/blog/linking-linux-explained)
- [@article@Diferença entre link hard e soft](https://kerneltalks.com/commands/difference-between-hard-link-and-soft-link/)
- [@article@Como entender a diferença entre Hard e Symbolic Links no Linux](https://labex.io/tutorials/linux-how-to-understand-the-difference-between-hard-and-symbolic-links-in-linux-409929)
