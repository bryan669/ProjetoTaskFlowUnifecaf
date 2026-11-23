import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Banco de dados em memória simulando tarefas da startup de logística
tarefas = [
    {
        "id": 1,
        "titulo": "Roteirizar frota Sudeste",
        "prioridade": "Crítica",
        "status": "Em Progresso",
    },
    {
        "id": 2,
        "titulo": "Atualizar rastreio de cargas",
        "prioridade": "Normal",
        "status": "A Fazer",
    },
]
proximo_id = 3


def validar_tarefa(titulo: str, prioridade: str) -> bool:
    """Valida se o título não está vazio e se a prioridade é permitida."""
    if not titulo or not titulo.strip():
        return False
    if prioridade not in ["Baixa", "Normal", "Crítica"]:
        return False
    return True


@app.route("/", methods=["GET"])
def index():
    """Rota principal: lista tarefas e aplica filtro opcional (Mudança de Escopo)."""
    filtro_prioridade = request.args.get("prioridade", "Todas")
    if filtro_prioridade != "Todas":
        lista_filtrada = [t for t in tarefas if t["prioridade"] == filtro_prioridade]
    else:
        lista_filtrada = tarefas
    return render_template(
        "index.html", tarefas=lista_filtrada, filtro_atual=filtro_prioridade
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    """Cria uma nova tarefa (Create)."""
    global proximo_id
    titulo = request.form.get("titulo", "").strip()
    prioridade = request.form.get("prioridade", "Normal")

    if validar_tarefa(titulo, prioridade):
        tarefas.append({
            "id": proximo_id,
            "titulo": titulo,
            "prioridade": prioridade,
            "status": "A Fazer",
        })
        proximo_id += 1
    return redirect(url_for("index"))


@app.route("/avancar/<int:tarefa_id>", methods=["POST"])
def avancar_status(tarefa_id: int):
    """Atualiza o status da tarefa no fluxo ágil (Update)."""
    fluxo = {"A Fazer": "Em Progresso", "Em Progresso": "Concluído"}
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id and tarefa["status"] in fluxo:
            tarefa["status"] = fluxo[tarefa["status"]]
            break
    return redirect(url_for("index"))


@app.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir(tarefa_id: int):
    """Remove uma tarefa do quadro (Delete)."""
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
