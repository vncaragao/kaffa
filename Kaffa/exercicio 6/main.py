import json, requests

response = requests.get("http://worldclockapi.com/api/json/utc/now")
json_conteudo = response.content
json_dados = json.loads(json_conteudo)
json_formatado = json.dumps(json_dados, indent=2)
print(json_formatado)