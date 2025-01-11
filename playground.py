from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import phi.api 
import phi
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app

import os
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

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

app = Playground(agents=[web_search_agent,finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)