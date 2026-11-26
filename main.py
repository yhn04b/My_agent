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
        "content": "First use the add tool to calculate 125 + 378.Then use the add tool again to add 100 to the previous tool result."
    }
]

total_tokens = 0
MAX_STEPS = 5

if __name__ == "__main__":
    
    for i in range(1, MAX_STEPS + 1):

        print(f"\n---Step{i}---")

        response = call_model(messages)
        total_tokens += response.usage.total_tokens
        model_output = response.choices[0].message.content
        action = process_action(model_output)
        print("Model output: ", model_output)

        if "tool" in action and "arguments" in action:
            observation = execute_tool(
                action["tool"], 
                **action["arguments"]
                )

            print("Observation: ", observation)
            
            messages.extend([
                {
                    "role": "assistant",
                    "content": model_output
                },
                {
                    "role": "user",
                    "content": f"observation: {observation}"
                }
            ])
        elif "answer" in action:
            print("Final Answer: ", action["answer"])
            break
        else:
            print(response)
            print("Invalid Output")
            break
    else:
        print("Maximum steps reached.")
    print("Total tokens = ", total_tokens)