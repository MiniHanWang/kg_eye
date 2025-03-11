from openai import OpenAI

# 设置 API 密钥
api_key = "**********************************"
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "希望你能够准确回答医学的眼科问题"},
    {"role": "user", "content": "我最近眼睛一直畏光。我在遇到风时大部分时间会出现眼睛不适好的治疗和保护。"}
  ]
)

print(completion.choices[0].message)