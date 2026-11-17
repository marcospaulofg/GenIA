from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.google import Gemini
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb

db = SqliteDb(
    db_file="tmp/agent.db",
    session_table="agent_sessions",
    memory_table="user_memories", # Tabela onde os fatos sobre o usuário ficam salvos
)

agent = Agent(
    name="Agente com Memória",
    model = Gemini(id="gemini-3.1-flash-lite"),
    tools = [TavilyTools()],
    db=db,
    user_id="marcospaulofg@gmail.com",
    description="Você é um pesquisador. Responda sempre chamando o usuário de 'senhor(a)'.",
    instructions=[
        "Use sempre a ferramenta de busca para obter dados em tempo real.",
        "Priorize o resumo (Summary) dos resultados da busca e ignore datas antigas de páginas indexadas.",
        "Se a ferramenta falhar, informe o erro e nunca invente valores.",
    ],
    enable_agentic_memory=True,
    add_datetime_to_context=True,
    debug_mode=True,
    markdown=True
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve('31_memory:app',reload=True)