tarefas = []

def adicionar_tarefa(tarefa):
    nova_tarefa = (tarefa, "Não concluída")
    tarefas.append(nova_tarefa)

def listar_tarefas(tarefa):
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa[0]} - Status: {tarefa[1]}")

def concluir_tarefa(tarefa):
    global tarefas
    tarefas = [ (t[0], "Concluída") if t[0] == tarefa else t for t in tarefas]

adicionar_tarefa("Arrumar o quarto")
adicionar_tarefa("Estudar para a prova")
listar_tarefas(tarefas)

print()

print("Agora vamos começar a concluir algumas tarefas...\n")

concluir_tarefa("Arrumar o quarto")
concluir_tarefa("Estudar para a prova")
listar_tarefas(tarefas)

