# 📚 CRUD de Cadastro de Alunos — Projeto Flask

> Um projeto simples e elegante em **Flask** para gerenciar o cadastro de alunos (Create, Read, Update, Delete). Ideal para aprendizado e como base para projetos maiores.

---

## ✨ Visão geral

Aplicação web minimalista que fornece um serviço CRUD para alunos. A estrutura do projeto é propositalmente simples para facilitar o entendimento:

```
/ (raiz do projeto)
│
├─ app.py           # ponto de entrada da aplicação
├─ requirements.txt # dependências (opcional)
├─ static/          # arquivos estáticos (CSS, JS, imagens)
└─ templates/       # templates Jinja2 (HTML)
```

> A ideia é usar o mínimo de arquivos para focar na lógica do Flask: rotas, templates e persistência simples (SQLite ou até uma lista em memória para fins didáticos).

---

## 🚀 Funcionalidades

* Listar todos os alunos
* Adicionar novo aluno
* Editar aluno existente
* Remover aluno
* Validação básica de formulários

---

## 🧭 Tecnologias

* Python 3.8+
* Flask (microframework)
* SQLite (recomendado para desenvolvimento) — opcional: SQLAlchemy para abstração
* Jinja2 para templates
* HTML / CSS simples (arquivos em `static/`)

---

## 🔧 Instalação (local)

1. Clone o repositório:

```bash
git clone <url-do-repo>
cd nome-do-repo
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
# se não houver requirements, instale o Flask:
pip install flask
```

4. Execute a aplicação:

```bash
# rodar em modo de desenvolvimento
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Windows PowerShell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```

Abra `http://127.0.0.1:5000` no navegador.

---

## 🗂 Estrutura sugerida dos templates

* `templates/index.html` — lista de alunos com botões para editar/excluir
* `templates/add.html` — formulário para criar um novo aluno
* `templates/edit.html` — formulário para editar um aluno existente
* `templates/base.html` — layout base (header, footer, bloco `content`)

---

## 🧾 Modelo de dados (sugestão)

Um aluno pode ter campos simples, por exemplo:

```txt
id (inteiro, auto-increment)
nome (string)
email (string)
idade (inteiro)
rg (string)
```
