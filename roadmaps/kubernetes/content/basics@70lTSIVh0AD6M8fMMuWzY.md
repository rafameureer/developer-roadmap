# Básicos de Agendamento

O agendamento envolve atribuir pods a nós trabalhadores com base em critérios como disponibilidade de recursos, rótulos, regras de afinidade/antiafinidade, sujeira e tolerâncias. Os pods são os unidades mínimas de implantação no k8s, composto por um ou mais contêineres que compartilham o mesmo espaço de nome de rede. O agendador é responsável por atribuir pods a nós, enquanto rótulos são usados para correspondência. As regras de afinidade e antiafinidade determinam como os pods são agendados com base em suas relações com outros pods ou nós. QoS é usado para priorizar o agendamento de pods com base em seus requisitos de recursos.

Acesse os seguintes recursos para saber mais:

- [@official@Agendador do Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [@video@Como funciona o Agendamento no Kubernetes](https://www.youtube.com/watch?v=0FvQR-0tK54)
