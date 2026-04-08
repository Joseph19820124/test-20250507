import re
import sys
from openai import OpenAI

prompt = sys.argv[1] if len(sys.argv) > 1 else "请用中文介绍一下你自己。"

client = OpenAI(
    api_key="EMPTY",
    base_url="http://127.0.0.1:8000/v1",
)

stream = client.chat.completions.create(
    model="qwen3-14b-awq",
    messages=[
        {
            "role": "system",
            "content": "Directly answer the user. Do not output chain-of-thought, reasoning process, or <think> tags.",
        },
        {"role": "user", "content": prompt},
    ],
    temperature=0.7,
    max_tokens=256,
    stream=True,
)

full_text = ""
printed = 0

for chunk in stream:
    delta = chunk.choices[0].delta.content or ""
    if not delta:
        continue

    full_text += delta
    clean_text = re.sub(r"<think>.*?</think>\s*", "", full_text, flags=re.S)

    if len(clean_text) > printed:
        new_text = clean_text[printed:]
        print(new_text, end="", flush=True)
        printed = len(clean_text)

print()
