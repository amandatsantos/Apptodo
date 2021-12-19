from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from datetime import date, datetime





app = FastAPI()


class Todo(BaseModel):
    id: Optional[str]
    terefas:str
    dia_de_criacao: Optional[str]
    descricao: Optional [str]
    realizada: bool
    prazo: Optional[str]

data : List[Todo] = []

@app.post('/inserir')
def inserir(todo: Todo):
    try:
        todo.id = str(uuid4())
        todo.dia_de_criacao= str(date.today())
        data.append(todo)
        return {'status': 'sucesso'}
    except:
        return{'status':'erro'}


@app.get('/listar')
def inserir(opcao: int = 0):
    if opcao == 0:
        return data
    elif opcao ==1:
        return list(filter(lambda x: x.realizada == False, data))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, data))

@app.get('/listagemUnica/{todo_id}')
def obter_tarefa(todo_id: str):
    for todo in data:
        if todo.id == todo_id:
            return todo
    return {"error": "tarefa não encontrada"}


@app.post('/alterarStatus')
def alteraStatus(id:int):
    try:
        data[id].realizada = not data[id].realizada
        return{'status' : 'sucesso'}
    except:
        return{'status':'erro'}


@app.delete('/deletar-tarefa/{todo_id}')
def remover_tarefa(todo_id: str):
    #buscar apossição da tarefa na lista
    for index, tarefa in enumerate(data):
        if todo_id == todo_id:
            posicao = index
            break
    if posicao != -1:
            data.pop(posicao) 
            return{'mensagem': f'{tarefa} \n tarefa removida com sucesso!'}
    else:
        return {'error': 'tarefa não encontrada'}