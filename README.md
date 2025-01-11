# Finance_Agent_Using_Phidata

A powerful AI-powered application that combines web search and financial analysis capabilities using Groq LLM and Phi framework.

## 🌟 Features

- **Web Search Agent**: Performs comprehensive web searches and generates NYT-style articles
- **Finance Agent**: Analyzes stock market data and provides financial insights
- **Multi-Agent System**: Combines both agents for complex queries
- **Interactive Playground**: Web interface to interact with the agents

## 🚀 Getting Started

## Prerequisites

Make sure you have Python installed and the following packages:
- pandas
- cassandra-driver
- phidata
- python-dotenv
- yfinance
- duckduckgo-search
- fastapi
- uvicorn
- groq
- os-sys
- dotenv
- python-docx (optional , if you face error)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nottarun7/Finance_Agent_Using_Phidata.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory with your API keys:
```bash
GROQ_API_KEY="your_groq_api_key"
PHI_API_KEY="your_phi_api_key"
```
4. Usage
### Running the Playground
```bash
python playground.py
```
This will start a local server with the playground interface where you can interact with both agents.

## Using Individual Agents
### You can also use the agents directly in your code:
```python
from agent import web_search_agent, finance_agent, multi_agent
```
### Use web search agent
```python
web_search_agent.print_response("Your query here")
```
### Use finance agent
```python
finance_agent.print_response("Get NVIDIA stock analysis")
```
### Use multi-agent system
```python
multi_agent.print_response("Summarize analyst recommendation and share the latest news for NVIDIA")
```

## 🔧 Agent Capabilities

### Web Search Agent
- Searches for top 5 relevant links
- Extracts and analyzes article content
- Generates NYT-style articles
- Includes source citations

### Finance Agent
- Real-time stock price information
- Analyst recommendations
- Stock fundamentals analysis
- Data presented in markdown tables

## 🛠️ Built With
- [Phi Framework](https://github.com/phidata-public/phi)
- [Groq LLM](https://groq.com/)
- [DuckDuckGo Search API](https://duckduckgo.com/)
- [YFinance](https://github.com/ranaroussi/yfinance)
- FastAPI

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Security Note
Never commit your API keys to version control. Always use environment variables or a secure secrets management system.
