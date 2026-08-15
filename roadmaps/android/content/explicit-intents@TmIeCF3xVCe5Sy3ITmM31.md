# Intenções Explícitas

**Intenções Explícitas** são principalmente usadas dentro dos limites de uma aplicação. Em intenções explícitas, você especifica o componente que precisa responder à intenção. Portanto, o componente-alvo deve ser especificado chamando métodos como `setComponent(ComponentName)`, `setClass(Context, Class)` ou `setClassName(String, String)`. Isso significa que as intenções explícitas são tipicamente usadas para iniciar atividades, enviar mensagens de broadcast e iniciar serviços dentro da aplicação. As intenções explícitas não são resolvidas pelo sistema, mas são passadas ao componente identificado na intenção.

Acesse os seguintes recursos para saber mais:

- [@oficial@Intenções Explícitas](https://developer.android.com/guide/components/intents-filters#explicit)
