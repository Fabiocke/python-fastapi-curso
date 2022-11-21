from email.policy import default
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path, Query
from typing import Optional

from models import Curso
from fastapi.responses import JSONResponse, Response

app = FastAPI()
cursos = {
    1: {
        'titulo': 'C1',
        'aulas': 112,
        'horas': 58
    },

    2: {
        'titulo': 'C2',
        'aulas': 87,
        'horas': 67
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{id_curso}')
async def get_curso(id_curso: int = Path(default = None, title='ID do curso',
                        description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[id_curso]
        curso.update({'id': id_curso})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                 detail = 'Curso não encontrado')
    

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = int(max(cursos)) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        del curso.id
        cursos[curso_id] = curso
        return curso
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                 detail = 'Curso não encontrado')
    

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                 detail = 'Curso não encontrado')



@app.get('/calculadora')
async def calcular(a: int, b: int, c: int = Query(default = None, gt=5)):
    c=c if c else 0
    resultado = a + b + c
    return {'resultado': resultado}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)


