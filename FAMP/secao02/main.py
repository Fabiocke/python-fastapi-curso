from fastapi import FastAPI

app = FastAPI()

@app.get('/msgs')
async def raiz():
    return {'msg': 'FastAPI no meu rabo'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host = '0.0.0.0', port=8000, log_level = 'info', reload = True)


    