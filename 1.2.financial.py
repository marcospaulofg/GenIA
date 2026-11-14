from agno.agent import Agent
#from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model = Gemini(id="gemini-3.1-flash-lite"),
    tools = [YFinanceTools()],
    instructions=[
        "Use sempre a ferramenta de busca para obter dados em tempo real.",
        "Se a ferramenta falhar, informe o erro e nunca invente valores.",
        "Use tabelas para fornecer a informação final. Não inclua nenhum outro texto."
    ]
)

agent.print_response("Qual é a cotação atual da Apple?", stream=True)