from password import password
import requests, json

question = input('Digite a sua pergunta: ')

headers = {"Authorization": f"Bearer {password}", "content-type": "application/json"}

id_modelo = "gpt-3.5-turbo-0301"
link = "https://api.openai.com/v1/chat/completions"

body_mensagem = {
    "model": id_modelo,
    "messages": [
        {
            "role": "user", "content": question
        }
    ]
}

body_mensagen = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagen)

resposta = requisicao.json()

mensagem = resposta["choices"][0]["message"]["content"]

print(mensagem)


