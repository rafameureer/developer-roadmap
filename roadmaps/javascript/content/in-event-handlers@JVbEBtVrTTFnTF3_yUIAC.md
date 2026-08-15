# Em manipuladores de eventos

Em um manipulador de evento anexado a um elemento DOM, `this` se refere ao elemento que recebeu o evento. Por exemplo, em um manipulador de clique, `this` é o botão ou elemento que foi clicado. As funções de seta não têm seu próprio `this`, então elas o herdam do escopo circundante.
