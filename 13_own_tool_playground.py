from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.google import Gemini
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
load_dotenv()



def celsius_to_fahrenheit(celsius: float):
    """Converte uma temperatura de graus Celsius para graus Fahrenheit.

    Args:
        celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura convertida em graus Fahrenheit.
    """

    return (celsius * 9/5) + 32

db = SqliteDb(
    session_table="agent_sessions",
    db_file="tmp/agent.db",
)

agent = Agent(
    name="Agente do tempo",
    model = Gemini(id="gemini-3.1-flash-lite"),
    tools = [TavilyTools(),
             celsius_to_fahrenheit],
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    instructions=[
        "Use sempre a ferramenta de busca para obter dados em tempo real.",
        "Priorize o resumo (Summary) dos resultados da busca e ignore datas antigas de páginas indexadas.",
        "Se a ferramenta falhar, informe o erro e nunca invente valores.",
    ],
    debug_mode=True
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve('13_own_tool_playground:app',reload=True)
                          

#agent.print_response("Pesquise a temperatura atual do Rio de Janeiro em graus Fahrenheit.")
