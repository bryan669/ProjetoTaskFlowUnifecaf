import pytest
from src.app import app, validar_tarefa, tarefas


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_validar_tarefa_valida():
    assert validar_tarefa("Entregar carga urgente", "Crítica") is True


def test_validar_tarefa_titulo_vazio():
    assert validar_tarefa("   ", "Normal") is False


def test_validar_tarefa_prioridade_invalida():
    assert validar_tarefa("Conferir estoque", "Urgentíssima") is False


def test_rota_principal_carrega(client):
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert b"TechFlow Solutions" in resposta.data


def test_adicionar_e_filtrar_tarefa(client):
    total_inicial = len(tarefas)
    client.post("/adicionar", data={"titulo": "Auditoria Frota", "prioridade": "Crítica"})
    assert len(tarefas) == total_inicial + 1

    resposta_filtro = client.get("/?prioridade=Crítica")
    assert b"Auditoria Frota" in resposta_filtro.data
