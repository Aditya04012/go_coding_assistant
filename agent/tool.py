from tools.rag_tool import search_go_kb
from tools.web_search_tool import web_seach
from tools.git_search import github_code_search

tools=[
    search_go_kb,
    web_seach,
    github_code_search,   
]