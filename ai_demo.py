# ai_demo.py AI调用演示脚本
# 两种模式：线上DeepSeek API / 本地Ollama DeepSeek（后面切换）
import requests

# ========== 配置区域 ==========
# 模式开关，"online" 线上API，"local"本地Ollama
mode = "online"

# 线上DeepSeek API配置
online_api_url = "https://api.deepseek.com/v1/chat/completions"
online_api_key = "在此填写你的DeepSeek API密钥"
online_model = "deepseek-chat"

# 本地Ollama配置（后面部署本地模型启用）
local_api_url = "http://localhost:11434/api/generate"
local_model = "deepseek:7b"

# 用户提问
user_question = "帮我解释Python函数是什么"
# ==============================

if mode == "online":
    # 调用线上DeepSeek
    msg = [{"role":"user", "content": user_question}]
    payload = {
        "model": online_model,
        "messages": msg,
        "temperature":0.7
    }
    res = requests.post(online_api_url, headers={"Authorization":f"Bearer {online_api_key}"}, json=payload)
    data = res.json()
    answer = data["choices"][0]["message"]["content"]
    print("【线上DeepSeek回答】")
    print(answer)

elif mode == "local":
    # 调用本地Ollama DeepSeek（后面启用）
    payload = {
        "model": local_model,
        "prompt": user_question,
        "stream": False
    }
    res = requests.post(local_api_url, json=payload)
    data = res.json()
    answer = data["response"]
    print("【本地Ollama DeepSeek回答】")
    print(answer)

