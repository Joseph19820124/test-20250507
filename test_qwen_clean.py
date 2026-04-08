import re
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://127.0.0.1:8000/v1",
)

resp = client.chat.completions.create(
    model="qwen3-14b-awq",
    messages=[
        {
            "role": "system",
            "content": "Directly answer the user. Do not output chain-of-thought, reasoning process, or <think> tags.",
        },
        {"role": "user", "content": "请用中文介绍一下你自己。"},
    ],
    temperature=0.7,
    max_tokens=256,
)

text = resp.choices[0].message.content or ""
text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.S)
print(text)
