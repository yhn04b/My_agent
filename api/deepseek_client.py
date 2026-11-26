import os
from openai import OpenAI
from api.check_key import get_api_key

client = OpenAI(
    api_key=get_api_key(),
    base_url="https://api.deepseek.com"
)
# 目前虽然避免了每次启动shell之后在终端输入api, 
# 但也导致每次运行main时都得输入api, 后续会考虑优化

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
