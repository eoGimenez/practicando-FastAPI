from fastapi import APIRouter, Depends
from fastapi.requests import Request

router = APIRouter(
    prefix='/dependencies',
    tags=['dependencies']
)


def convert_header(request: Request, separator: str = '~~'):
    destruct_header = []
    for key, value in request.headers.items():
        destruct_header.append(f'{key} {separator} {value}')
    return destruct_header


@router.get('/')
def get_items(separator: str = '~~', headers=Depends(convert_header)):
    return {
        'items': [{'ball': '3.4'}, {'bike': '244'}],
        'headers': headers
    }


@router.post('/')
def create_item(headers=Depends(convert_header)):
    return {
        'result': 'New item created',
        'headers': headers
    }


class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


@router.post('/user')
def create_user(name: str, email: str, password: str, account: Account = Depends()):
    return {
        'name': account.name,
        'email': account.email
    }
