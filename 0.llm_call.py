#from agno.models.openai import OpenAIChat
#from agno.models.groq import Groq
from agno.models.google import Gemini
from agno.models.message import Message

from dotenv import load_dotenv
load_dotenv()

model = Gemini(
    id="gemini-3.1-flash-lite"
)

msg = Message(
    role="user",
    content = "Olá, meu nome é Marcos, Tudo bem?"
)

response = model.response(messages = [msg])

print(response.content)