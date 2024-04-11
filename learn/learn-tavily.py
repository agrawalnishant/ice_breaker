import os
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv

load_dotenv()


# set up the agent
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

# initialize the agent
agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# run the agent
search_res = agent_chain.run(
    "Who is nishant  at Apptio?. Give info only about the nishant having more experience."
)

print(search_res)
