# TechFlow Solutions — Sistema Ágil de Gerenciamento de Tarefas

## 1. Objetivo e Escopo Inicial
Sistema web desenvolvido pela **TechFlow Solutions** para uma startup de logística acompanhar o fluxo de trabalho em tempo real, priorizar entregas críticas e monitorar o andamento operacional via quadro Kanban (CRUD de tarefas).

## 2. Metodologia Adotada
Foi utilizado um modelo ágil híbrido (**Scrum + Kanban**), organizando o backlog em sprints curtas e controlando o fluxo contínuo na aba **GitHub Projects** nas colunas *To Do (A Fazer)*, *In Progress (Em Progresso)* e *Done (Concluído)*.

## 3. Como Executar Localmente
```bash
pip install -r requirements.txt
python -m src.app
```
Acesse `http://127.0.0.1:5000` no navegador. Para rodar os testes:
```bash
pytest -v
```

## 4. Gestão de Mudanças (Alteração de Escopo)
- **Solicitação do Cliente:** Durante a validação da primeira entrega, a startup de logística identificou a necessidade de isolar visualmente gargalos operacionais urgentes.
- **Mudança Implementada:** Adição de um **filtro dinâmico por nível de prioridade (`Crítica`, `Normal`, `Baixa`)** na tela principal (`GET /?prioridade=...`).
- **Impacto no Kanban:** Criação de novo card no backlog (*"Implementar filtro por prioridade crítica"*), priorizado e concluído sem comprometer as entregas principais.
