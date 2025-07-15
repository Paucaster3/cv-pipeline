import requests

LS_API_URL = "http://labelstudio_host:8080/api"
LS_API_TOKEN = "TU_TOKEN"

headers = {"Authorization": f"Token {LS_API_TOKEN}"}

# Listar proyectos
resp = requests.get(f"{LS_API_URL}/projects", headers=headers)
print(resp.json())

# Exportar anotaciones de un proyecto
project_id = 1
export = requests.get(
    f"{LS_API_URL}/projects/{project_id}/export?exportType=YOLO",
    headers=headers
)
with open("export_yolo.zip", "wb") as f:
    f.write(export.content)
