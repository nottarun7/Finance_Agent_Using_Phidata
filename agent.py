from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search web for the information",
    model=Groq(id="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
        "Always show the source"
    ],
    show_tool_calls = True,
    markdown = True,
    )

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls = True,
    markdown = True,
)

multi_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-8b-8192"),
    instructions=["Include sources","Use table format to display data"],
    show_tool_calls = True,
    markdown = True,
)

multi_agent.print_response("Summarize analyst recomendation and share the latest news for NVIDIA",stream=True)