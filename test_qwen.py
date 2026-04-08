from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://127.0.0.1:8000/v1",
)

resp = client.chat.completions.create(
    model="qwen3-14b-awq",
    messages=[
        {"role": "user", "content": "请用中文介绍一下你自己。"}
    ],
    temperature=0.7,
    max_tokens=256,
)

print(resp.choices[0].message.content)
