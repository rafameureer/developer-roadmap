# Contando Documentos

Contar documentos no MongoDB usa métodos como `countDocuments()` para contagens filtradas precisas e `estimatedDocumentCount()` para totais aproximados rápidos. O `countDocuments()` suporta filtros de consulta e fornece resultados precisos, mas pode ser mais lento em coleções grandes. O `estimatedDocumentCount()` usa metadados da coleção para estimativas rápidas, tornando-o ideal para métricas do painel e estatísticas rápidas.

Acesse os seguintes recursos para saber mais:

- [@oficial@Contando Documentos](https://www.mongodb.com/docs/manual/reference/method/db.collection.countdocuments/)
- [@oficial@estimatedDocumentCount](https://www.mongodb.com/docs/manual/reference/method/db.collection.estimateddocumentcount/)
