# Ponteiros Inteligentes

Ponteiros inteligentes são classes que se comportam como ponteiros regulares, mas fornecem gerenciamento automático de memória. Eles ajudam a prevenir vazamentos de memória ao automaticamente desalocar a memória às quais eles apontam quando não forem mais necessários. Isso é feito através de técnicas como contagem de referências e RAII (Aquisição de Recursos é Inicialização). Em essência, encapsulam um ponteiro bruto e garantem que a memória para o qual ele aponta seja liberada quando o ponteiro inteligente sai do escopo ou é resetado.

Visite os seguintes recursos para aprender mais:

- [@artigo@Ponteiros Inteligentes](https://en.cppreference.com/book/intro/smart_pointers)
- [@vídeo@PONTEIROS INTELIGENTES em C++ (std::unique_ptr, std::shared_ptr, std::weak_ptr)](https://www.youtube.com/watch?v=UOB7-B2MfwA)
