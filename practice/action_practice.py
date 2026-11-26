import json
from practice import practice1

model_output = """
{
    "tool": "search",
    "arguments": {
        "query": "ReAct论文"
    }
}
"""

def process_action(model_output):
    output = json.loads(model_output)
    return  practice1.execute_tool(
            output["tool"],
            **output["arguments"]
        )

if __name__ == "__main__":
    print(process_action(model_output))

    print(process_action(
        '{"tool": "add", "arguments": {"a": 8, "b": 9}}'
    ))

    print(process_action(
        '{"tool": "get_date", "arguments": {}}'
    ))