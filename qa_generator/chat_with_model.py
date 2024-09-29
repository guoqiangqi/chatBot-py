import requests
# 问题生成函数
def chat_with_model(llm_url,llm_token,llm_method,content,question):
   headers = {
        "Authorization": llm_token,
        "Content-Type": "application/json",
    }
   data = {
        "model": llm_method,
        "messages": [
            {"role": "system", "content": content},
            {"role": "user", "content": question}
        ]
    }
   response = requests.post(llm_url, headers=headers, json=data)
   if response.status_code == 200:
        return response.json()["choices"][0]["message"]['content']
   else:
        return ''
