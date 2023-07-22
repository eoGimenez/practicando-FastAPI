from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()

# creando un enum de variables en el path


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/type/{type}')
async def blog_type(type: BlogType):
    print(type.value)
    return {"message": f"Blog type: {type.value}"}

# para manejar el status de la respuesta.

@app.get('/{id}', status_code=status.HTTP_200_OK)
async def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id: {id}'}
