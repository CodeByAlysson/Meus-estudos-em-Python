tarefas = []

def adicionar_tarefa(tarefa):
    nova_tarefa = (tarefa, "Não concluída")
    tarefas.append(nova_tarefa)

def listar_tarefas(tarefa):
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa[0]} - Status: {tarefa[1]}")

adicionar_tarefa("Arrumar o quarto")
listar_tarefas(tarefas)