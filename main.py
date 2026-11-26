from api.deepseek_client import call_model
from practice.action_practice import process_action
from practice.practice1 import execute_tool
from prompts.react import SYSTEM_PROMPT

messages = [
    {
        "role": "system", 
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user", 
        "content": "Calculate 125 + 378"
    }
]

if __name__ == "__main__":
    response = call_model(messages)
    action = process_action(response)
    observation = execute_tool(
            *action["tool"], 
            **action["arguments"]
        )
    print(response, "\n", observation, "\n", response.usage.total_tokens)