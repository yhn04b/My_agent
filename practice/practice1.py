def add(a, b):
    return a + b

def search(query):
    return "搜索：" + query

def get_date():
    return "模拟日期"

tools = {
    "add": add,
    "search": search,
    "get_date": get_date
}

def execute_tool(tool_name, *args, **kwargs):
    return tools[tool_name](*args, **kwargs)

if __name__ == "__main__":
    print(execute_tool("add", 3, 5))

    print(execute_tool("add", a=10, b=20))

    print(execute_tool("search", query="ReAct"))

    print(execute_tool("get_date"))