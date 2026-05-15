from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home ():
    return {
        "Mensagem": "API FastAPI",
        }

@app.get("/health")
def health():
    return {
        "Status": "online"
    }

@app.get("/soma")
def soma(a: int, b: int):
    return {"Resultado": a + b}
    
from pydantic import BaseModel
class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.post("/tarefas")
def criar_tarefa(tarefa : Tarefa):
    return {
        "mensagem": "Tarefa recebida com sucesso",
        "dados": tarefa
    }