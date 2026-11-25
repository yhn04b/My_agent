def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

tools = {
    "add": add,
    "multiply": multiply
}

action = {
    "tool": "multiply",
    "arguments": {
        "a": 6,
        "b": 7
    }
}

def execute(tool, *args, **kwargs):
    return tools[tool](*args, **kwargs)

print(execute(action["tool"], **action["arguments"]))