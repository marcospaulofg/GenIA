from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model = Gemini(id="gemini-3.1-flash-lite"),
    tools = [TavilyTools()],
    add_datetime_to_context=True,
    instructions=[
        "Use sempre a ferramenta de busca para obter dados em tempo real.",
        "Priorize o resumo (Summary) dos resultados da busca e ignore datas antigas de páginas indexadas.",
        "Se a ferramenta falhar, informe o erro e nunca invente valores.",
    ],
    debug_mode=True,
    markdown=True
)

agent.print_response("quais as principais notícias do Rio de Janeiro hoje?")
