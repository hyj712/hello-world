import os
from openai import OpenAI

key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=key,base_url="https://api.deepseek.com")

res = client.chat.completions.create(model="deepseek-flash",
                                     messages=[{"role":"user","content":""}]

)
print(res.choices[0].message.content)
