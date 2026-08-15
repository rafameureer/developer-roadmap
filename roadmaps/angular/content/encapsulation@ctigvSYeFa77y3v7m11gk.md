# Encapsulamento

Política de encapsulamento para o estilo do componente. Valores possíveis:

*   `ViewEncapsulation.Emulated`: Aplica estilos modificados do componente para emular um comportamento de encapsulamento CSS nativo Shadow DOM.
*   `ViewEncapsulation.None`: Aplica estilos do componente globalmente sem qualquer tipo de encapsulamento.
*   `ViewEncapsulation.ShadowDom`: Usa a API nativa do Shadow DOM do navegador para encapsular estilos.

Se não for fornecido, o valor é tomado das opções do compilador, que padrão para `ViewEncapsulation.Emulated`.

Se a política for `ViewEncapsulation.Emulated` e o componente não tiver estilos nem {@link Component#styleUrls styleUrls}, a política é automaticamente alterada para `ViewEncapsulation.None`.

Acesse os seguintes recursos para saber mais:

- [@official@Escopo de Estilos](https://angular.dev/guide/components/styling#style-scoping)
- [@official@Component Encapsulamento](https://angular.dev/api/core/Component#encapsulation)
