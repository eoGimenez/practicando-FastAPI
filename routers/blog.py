from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])


@router.get('/all',
            summary='Devuelve todos los blogs',
            description='Esta api hace fetch a todos los blogs',
            response_description='Lista de blogs validos'
            )
async def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@router.get('/{id}/comments/{comment_id}',
            tags=["comments"],
            summary='Devuelve comentarios de blogs'
            )
async def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simula la devolucion de un comentario del blog

    - **id** parametro obligatorio
    - **comment_id** parametro obligatorio
    - **valid** parametro opcional
    - **username** parametro opcional
    """
    return {'message': f'blog_id: {id}, comment id: {comment_id}, valid: {valid}, username: {username}'}

# creando un enum de variables en el path


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
async def blog_type(type: BlogType):
    print(type.value)
    return {"message": f"Blog type: {type.value}"}

# para manejar el status de la respuesta.


@router.get('/{id}',
            status_code=status.HTTP_200_OK
            )
async def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id: {id}'}


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]

# asi podemos pasar los tres tipos de parametros, body, path y query en sus respectivos ordenes,


@router.post('/{id}')
def create_blog(blog_details: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog_details,
        'version': version
    }
