from collections import deque  # Importa deque para gerenciar filas e pilhas de forma eficiente.
import heapq  # Importa heapq para manipular filas de prioridade.
import time  # Importa time para medir tempos de execução.

# Classe principal que gerencia as tarefas.
class TaskManager:
    def __init__(self):
        # Inicializa uma fila para tarefas pendentes.
        self.pending_tasks = deque()
        # Inicializa uma pilha para o histórico de tarefas concluídas.
        self.completed_tasks = []
        # Inicializa uma tabela hash para mapear tarefas a seus responsáveis.
        self.task_map = {}
        # Inicializa uma fila de prioridade para tarefas, usada para reordenação.
        self.priority_queue = []
        # Inicializa o contador para o tempo total de conclusão das tarefas.
        self.total_completion_time = 0
        # Inicializa o contador para o número de tarefas concluídas.
        self.completed_count = 0

    # Método para adicionar uma nova tarefa ao sistema.
    def add_task(self, task_name, priority, responsible):
        """
        Adiciona uma nova tarefa.
        """
        # Cria um dicionário para armazenar os detalhes da tarefa.
        task = {
            "name": task_name,  # Nome da tarefa.
            "priority": priority,  # Prioridade da tarefa.
            "responsible": responsible,  # Responsável pela tarefa.
            "timestamp": time.time(),  # Registra o momento em que a tarefa foi criada.
        }
        # Adiciona a tarefa à fila de pendentes.
        self.pending_tasks.append(task)
        # Insere a tarefa na fila de prioridade com a prioridade invertida para ordenação.
        heapq.heappush(self.priority_queue, (-priority, task))
        # Mapeia o nome da tarefa ao responsável na tabela hash.
        self.task_map[task_name] = responsible
        # Imprime a confirmação da tarefa adicionada.
        print(f"Tarefa '{task_name}' adicionada com prioridade {priority} e responsável {responsible}.")

    # Método para concluir a próxima tarefa pendente.
    def complete_task(self):
        """
        Completa a próxima tarefa pendente.
        """
        # Verifica se há tarefas pendentes.
        if not self.pending_tasks:
            print("Nenhuma tarefa pendente para concluir.")
            return

        # Remove a próxima tarefa da fila de pendentes.
        task = self.pending_tasks.popleft()
        # Adiciona a tarefa concluída ao histórico.
        self.completed_tasks.append(task)
        # Calcula o tempo gasto para concluir a tarefa.
        completion_time = time.time() - task["timestamp"]
        # Incrementa o tempo total de conclusão.
        self.total_completion_time += completion_time
        # Incrementa o contador de tarefas concluídas.
        self.completed_count += 1
        # Imprime a confirmação da tarefa concluída e o tempo gasto.
        print(f"Tarefa '{task['name']}' concluída em {completion_time:.2f} segundos.")

    # Método para exibir as tarefas pendentes e concluídas.
    def view_tasks(self):
        """
        Exibe tarefas pendentes e concluídas.
        """
        # Imprime as tarefas pendentes.
        print("\nTarefas Pendentes:")
        for task in self.pending_tasks:
            print(f"- {task['name']} (Prioridade: {task['priority']}, Responsável: {task['responsible']})")

        # Imprime o histórico de tarefas concluídas.
        print("\nTarefas Concluídas:")
        for task in reversed(self.completed_tasks):  # Exibe na ordem inversa para mostrar as mais recentes primeiro.
            print(f"- {task['name']} (Responsável: {task['responsible']})")

    # Método para reordenar as tarefas pendentes com base na prioridade.
    def reorder_tasks(self):
        """
        Reordena as tarefas pendentes com base na prioridade.
        """
        # Ordena as tarefas por prioridade de forma decrescente e as armazena novamente na fila.
        self.pending_tasks = deque(
            sorted(self.pending_tasks, key=lambda x: -x["priority"])
        )
        print("Tarefas reordenadas por prioridade.")

    # Método para calcular o tempo médio de conclusão das tarefas.
    def calculate_average_completion_time(self):
        """
        Calcula o tempo médio para completar as tarefas.
        """
        # Verifica se há tarefas concluídas.
        if self.completed_count == 0:
            print("Nenhuma tarefa foi concluída ainda.")
            return
        # Calcula o tempo médio de conclusão.
        average_time = self.total_completion_time / self.completed_count
        print(f"Tempo médio de conclusão: {average_time:.2f} segundos.")

    # Método para reatribuir o responsável por uma tarefa.
    def assign_task(self, task_name, new_responsible):
        """
        Reatribui um responsável a uma tarefa.
        """
        # Verifica se a tarefa existe no mapa de tarefas.
        if task_name in self.task_map:
            # Atualiza o responsável pela tarefa.
            self.task_map[task_name] = new_responsible
            print(f"Tarefa '{task_name}' agora é responsabilidade de {new_responsible}.")
        else:
            print(f"Tarefa '{task_name}' não encontrada.")


# Bloco principal de execução do script.
if __name__ == "__main__":
    # Cria uma instância do gerenciador de tarefas.
    manager = TaskManager()

    # Adicionando tarefas ao sistema.
    manager.add_task("Planejar sprint", 2, "João")
    manager.add_task("Corrigir bugs", 5, "Maria")
    manager.add_task("Implementar nova funcionalidade", 3, "Ana")
    manager.add_task("Realizar testes unitários", 1, "Igor")
    manager.add_task("Atualizar Documentação", 3, "Bruna")

    # Exibe as tarefas pendentes e concluídas.
    manager.view_tasks()

    # Reordena as tarefas pendentes por prioridade e exibe novamente.
    manager.reorder_tasks()
    manager.view_tasks()

    # Conclui duas tarefas e exibe o estado atualizado.
    manager.complete_task()
    manager.complete_task()

    # Calcula o tempo médio de conclusão das tarefas.
    manager.calculate_average_completion_time()

    # Reatribui um responsável para uma tarefa e exibe o estado atualizado.
    manager.assign_task("Implementar nova funcionalidade", "Carlos")
    manager.view_tasks()
