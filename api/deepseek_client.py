import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def call_model(messages):
    return  client.chat.completions.create(
                model="deepseek-flash",
                messages=messages,
                stream=False,
                extra_body={"thinking": {"type": "disabled"}}
            )

if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "你是一个人工智能研究助手。"
        },
        {
            "role": "user",
            "content": "请简要介绍ReAct。"
        }
    ]

    response = call_model(messages)

    print(response.choices[0].message.content)
    print(response.usage.total_tokens)
