# Projeito_final_ED2
# Gerenciador de Tarefas em Projetos de Software

Este projeto implementa um sistema de gerenciamento de tarefas para projetos de software, utilizando diversas estruturas de dados avançadas, como pilhas, filas e tabelas hash. Além disso, o sistema permite ordenação por prioridade e cálculo do tempo médio para completar tarefas.

## Funcionalidades

1. **Adicionar tarefas**: Adicione tarefas com prioridade, responsável e timestamp.
2. **Visualizar tarefas**: Exiba a lista de tarefas pendentes e o histórico de tarefas concluídas.
3. **Reordenar tarefas**: Reorganize as tarefas pendentes com base na prioridade.
4. **Completar tarefas**: Marque tarefas como concluídas e registre o tempo de execução.
5. **Calcular tempo médio**: Calcule o tempo médio necessário para concluir as tarefas.
6. **Reatribuir responsável**: Altere o responsável por uma tarefa existente.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Estruturas de Dados**:
  - `deque` para filas e pilhas.
  - `heapq` para ordenação baseada em prioridade.
  - Dicionários para tabelas hash.

## Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado. Para verificar a versão do Python, execute:

```bash
python --version
