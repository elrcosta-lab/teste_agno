from agno.agent import Agent
from agno.models.lmstudio import LMStudio
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.os import AgentOS


agent = Agent(
    id="Agente de pesquisa",
    name="Pesquisador DDG",
    role="Um agente que pesquisa na web usando DuckDuckGo para responder perguntas dos usuários.",
    instructions=[
        "Use este agente para responder perguntas dos usuários pesquisando na web com DuckDuckGo.",
        "Busque as principais fontes confiáveis sobre o tema.",
        "Entregue uma saída concisa com: 5-10 fatos em bullets e um quadro de fontes com título + URL.",
        "Não invente links. Priorize sites oficiais, artigos e referências robustas.",
    ],
    model=LMStudio(id="deepseek/deepseek-r1-0528-qwen3-8b"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()
