from fastapi import APIRouter, Depends
from fastapi.requests import Request
from custom__log import log

router = APIRouter(
    prefix='/dependencies',
    tags=['dependencies'],
    dependencies=[Depends(log)]  # Global dependencie!
)


def convert_params(request: Request, separator: str = '--'):
    query = []
    for key, value in request.query_params.items():
        query.append(f'{key} {separator} {value}')
    return query


def convert_header(request: Request, separator: str = '~~', query=Depends(convert_params)):
    destruct_header = []
    for key, value in request.headers.items():
        destruct_header.append(f'{key} {separator} {value}')
    return {
        'headers': destruct_header,
        'query': query
    }


@router.get('/')
def get_items(separator: str = '~~', headers=Depends(convert_header)):
    return {
        'items': [{'ball': '3.4'}, {'bike': '244'}],
        'headers': headers
    }


@router.post('/')
def create_item(name: str, test: str, headers=Depends(convert_header)):
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
