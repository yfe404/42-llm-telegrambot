import os
import requests
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from typing import List

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

openai_api_key = os.environ.get('OPENAI_API_KEY')

@tool
def get_user_infos(user_id: str) -> str:
    """
    Returns the infos from 42 intra about a specific user.

    Rreturns string of user data
    """
    response = requests.get("http://api-wrapper:5000/connected")


@tool
def fetch_connected_users() -> str:
    """
    Fetches the list of currently connected users on the campus of 42 Prague.
    Returns JSON string of user data.
    """
    response = requests.get("http://api-wrapper:5000/connected")
    response.raise_for_status()
    return response.text


#model = ChatOllama(model="qwen3:1.7b")
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=openai_api_key
)


class Agent:
    def __init__(self):
        self.config = {"configurable": {"thread_id": "abc123"}}
        self.tools = [fetch_connected_users, get_user_infos]
        self.model = model
        self.memory = MemorySaver()
        self.agent_executor = create_react_agent(
                self.model, 
                self.tools, 
                checkpointer=self.memory
        )

    def get_response(self, query: str):
        response = self.agent_executor.invoke(
                {
                    "messages": [
                        HumanMessage(content=query)
                    ]}, self.config)
        print(response)
        return response["messages"][-1].content
