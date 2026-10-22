from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

web_search_tool = DuckDuckGoSearchRun()


@tool
def web_seach(query:str)->str:


    """Search the web for programming documentation, Go code examples,
    backend development concepts, APIs, and technical solutions.
    Use this tool when current or external information is needed.
    """

    try:
        result=web_search_tool.invoke(query)
        if not result or not result.strip():
            return "No relevent information found on web"

        return result

    except Exception as e:
        return f"Web search failed: {str(e)}"

    
   
