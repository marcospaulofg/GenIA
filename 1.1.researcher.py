from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model = Gemini(id="gemini-3.1-flash-lite"),
    tools = [TavilyTools()],
    instructions=[
        "Use sempre a ferramenta de busca para obter dados em tempo real.",
        "Se a ferramenta falhar, informe o erro e nunca invente valores.",
    ]
)

agent.print_response("Pesquise a temperatura atual do Rio de Janeiro e me diga se está quente ou frio.")
