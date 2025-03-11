# 使用curl命令测试返回
# curl -X POST "http://36.139.11.103:8000/v1/chat/completions" \
# -H "Content-Type: application/json" \
# -d "{\"model\": \"chatglm3-6b\", \"messages\": [{\"role\": \"system\", \"content\": \"You are ChatGLM3, a large language model trained by Zhipu.AI. Follow the user's instructions carefully. Respond using markdown.\"}, {\"role\": \"user\", \"content\": \"你好，给我讲一个故事，大概100字\"}], \"stream\": false, \"max_tokens\": 100, \"temperature\": 0.8, \"top_p\": 0.8}"

# 使用Python代码测返回
import requests
import json

base_url = "http://36.212.143.247:6000"
def create_chat_completion(model, messages, functions, use_stream=False):
    data = {
        "functions": functions,  # 函数定义
        "model": model,  # 模型名称
        "messages": messages,  # 会话历史
        "stream": use_stream,  # 是否流式响应
        "max_tokens": 3000,  # 最多生成字数
        "temperature": 0.8,  # 温度
        "top_p": 0.8,  # 采样概率
    }
    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        if use_stream:
            # 处理流式响应
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        print(content)
                    except:
                        print("Special Token:", decoded_line)
        else:
            # 处理非流式响应
            decoded_line = response.json()
            # print(decoded_line)
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            print(content)
    else:
        print("Error:", response.status_code)
        return None
def simple_chat(use_stream=True):
    functions = None
    chat_messages = [
        {
            "role": "system",
            "content": "医疗方向",
        },
        {
            "role": "user",
            "content": "干眼有什么症状"
        }
    ]
    create_chat_completion("chatglm3-6b", messages=chat_messages, functions=functions, use_stream=use_stream)


if __name__ == "__main__":
    # function_chat(use_stream=True)
    simple_chat(use_stream=False)
