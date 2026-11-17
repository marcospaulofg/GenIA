# 🤖 GenIA — Estudo com Agentes de IA e RAG

Repositório dedicado aos meus estudos em **Inteligência Artificial Generativa** e **Agentes Autônomos** utilizando Python e o framework **Agno**

---

## 🛠️ Stack & Tecnologias

* **Linguagem:** Python 3.13+
* **Gerenciador de Pacotes:** [uv](https://docs.astral.sh/uv/)
* **Framework de Agentes:** [Agno](https://docs.agno.com/) (`Agent`, `AgentOS`, `Knowledge`)
* **Modelos (LLMs):** Google Gemini (`gemini-3.1-flash-lite`) via `google-genai`
* **Banco Vetorial (RAG):** ChromaDB (persistência local)
* **Embeddings:** Sentence Transformers (`paraphrase-multilingual-MiniLM-L12-v2`)
* **Banco de Sessões & Memória:** SQLite (`SqliteDb` + `SQLAlchemy`)
* **Ferramentas (Tools):** TavilyTools, YFinanceTools e Custom Tools

---

## 📂 Estrutura do Projeto

```text
GenIA/
├── 0.llm_call.py                 # Chamada direta ao modelo Gemini via Agno
├── 1.1.researcher.py             # Agente pesquisador conectado à web (Tavily / YFinanceTools)
├── 13_own_tool_playground.py     # Agente com ferramentas customizadas, memória SQLite e AgentOS
├── 21_pdf_agent.py               # Agente especialista em PDF com pipeline RAG completo
├── GlobalEVOutlook2025.pdf       # Documento base utilizado nos testes de RAG
├── pyproject.toml                # Dependências e metadados do projeto
├── uv.lock                       # Lockfile de versões exatas das bibliotecas
└── .gitignore                    # Arquivos ignorados (venv, .env, bancos locais)