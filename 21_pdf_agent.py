from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.recursive import RecursiveChunking
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder

# 1. Banco vetorial com embedder multilíngue
vector_db = ChromaDb(
    collection="pdf_agent",
    path="tmp/chroma_db",
    persistent_client=True,
    embedder=SentenceTransformerEmbedder(id="paraphrase-multilingual-MiniLM-L12-v2"),
)

# 1.1 Criar uma base de conhecimento com o banco vetorial
knowledge = Knowledge(
    vector_db=vector_db
)

# 2. Leitor de PDF com chunking recursivo e overlap para preservar contexto entre blocos
pdf_reader = PDFReader(
    chunk=True,
    chunking_strategy=RecursiveChunking(
        chunk_size=1000,
        overlap=150
    )
)

# 2.1. Ingestão do documento (executada apenas se ainda não existir na coleção)
knowledge.insert(
    path="GlobalEVOutlook2025.pdf",
    reader=pdf_reader,
    skip_if_exists=True
)

# 3. Banco de dados para persistência do histórico de sessões
db = SqliteDb(
    session_table="agent_sessions",
    db_file="tmp/agent.db",
)

# 4. Agente com instruções de sistema
agent = Agent(
    name="Agente de PDF",
    model = Gemini(id="gemini-3.1-flash-lite"),
    db=db,
    knowledge=knowledge,
    search_knowledge=True,
    description="Agente especialista na análise do relatório Global EV Outlook 2025.",
    instructions=[
        "Responda às perguntas utilizando EXCLUSIVAMENTE as informações recuperadas da base de conhecimento.",
        "Se a resposta não estiver explicitamente presente nos trechos recuperados, diga claramente que não encontrou essa informação no documento. Nunca invente ou extrapole dados.",
        "Sempre que possível, cite números exatos, anos, países/regiões e o contexto do relatório para fundamentar sua resposta.",
        "Responda no mesmo idioma em que o usuário fizer a pergunta."
    ],
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    debug_mode=True
)

agent_os = AgentOS(agents=[agent], db=db)
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve('21_pdf_agent:app',reload=True)