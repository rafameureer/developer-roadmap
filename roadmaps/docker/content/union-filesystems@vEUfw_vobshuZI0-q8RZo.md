# Sistemas de Arquivos Unificados

Os sistemas de arquivos unificados (UnionFS) criam estruturas de arquivo virtual e em camadas overlayizando múltiplos diretórios sem modificar os originais. O Docker usa isso para gerenciar armazenamento eficientemente minimizando a duplicação e reduzindo o tamanho das imagens através de uma abordagem de sistema de arquivos em camadas que mantém o conteúdo dos diretórios separado enquanto estão montados juntos.

Acesse os seguintes recursos para saber mais:

- [@artigo@AUFS (Sistema de Arquivos Unificado Avançado)](http://aufs.sourceforge.net/)
- [@artigo@OverlayFS (Sistema de Arquivos Overlay)](https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html)
- [@artigo@Btrfs (Sistema de Arquivos B-Tree)](https://btrfs.readthedocs.io/en/stable/)
- [@artigo@ZFS (Sistema de Arquivos Z)](https://zfsonlinux.org/)
