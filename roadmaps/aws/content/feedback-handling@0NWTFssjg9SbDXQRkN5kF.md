# Tratamento de Feedback

O AWS Simple Email Service (SES) fornece um mecanismo para lidar com rejeições, reclamações e notificações de entrega. Este mecanismo é chamado de tratamento de feedback. As rejeições ocorrem quando um email não pode ser entregue a um destinatário. As reclamações acontecem quando um destinatário marca um email como spam. As notificações de entrega são enviadas quando o Amazon SES consegue entregar com sucesso um email para o servidor de correio do destinatário. O AWS SES permite que você receba essas notificações de feedback por email, relaying-as a um tópico do Amazon SNS ou através do Amazon CloudWatch. O processo de decidir qual ação tomar quando seus emails forem rejeitados ou marcados como spam é chamado de tratamento de feedback. O AWS SES lida automaticamente com todas as reclamações de loop de feedback (FBL), mas em relação às rejeições, você tem a flexibilidade de escolher como deseja que o seu sistema responda.

Acesse os seguintes recursos para saber mais:

- [@official@Reclamações](https://aws.amazon.com/ses/faqs)
