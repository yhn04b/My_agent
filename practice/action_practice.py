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
    return  output

if __name__ == "__main__":
    output = process_action(model_output)
    observation = practice1.execute_tool(
            output["tool"],
            **output["arguments"]
        )
    print(observation)

    print(
        practice1.execute_tool(
            process_action(
                '{"tool": "add", "arguments": {"a": 8, "b": 9}}'
            )["tool"], 
            **process_action(
                '{"tool": "add", "arguments": {"a": 8, "b": 9}}'
            )["arguments"]
        )
    )

