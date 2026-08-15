# Mapeamento Manual

O mapeamento de objetos manual no [ASP.NET](http://ASP.NET) Core significa atribuir explicitamente valores de um objeto para outro sem usar bibliotecas de terceiros como o AutoMapper. Esse abordagem dá a você o controle completo sobre como as propriedades são mapeadas e permite transformações personalizadas se necessário.

Por exemplo, se uma entidade **Employee** tiver propriedades como Id, Nome, Email e Departamento, e precisarmos convertê-la em um **EmployeeDTO** sem expor dados sensíveis como Id, um método de mapeamento manual pode selecionar apenas os campos necessários. No entanto, isso vem com desafios, como o aumento do código boilerplate e a necessidade de atualizações manuais sempre que o modelo de dados mudar. Em uma aplicação real do [ASP.NET](http://ASP.NET) Core, o mapeamento manual pode ser implementado usando métodos auxiliares estáticos ou métodos de extensão que recebem uma entidade como entrada e retornam um DTO, garantindo que a lógica de mapeamento permaneça centralizada e reutilizável em diferentes partes da aplicação.

Acesse os seguintes recursos para saber mais:

- [@artigo@Mapeamento manual vs Automático no ASP.NET?](https://medium.com/@anderson.buenogod/manual-vs-automated-mapping-in-c-which-approach-is-best-for-your-project-50de1fd73bfa)
