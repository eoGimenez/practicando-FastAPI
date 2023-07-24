from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        from_atributes = True


class User(BaseModel):
    id: int
    username: str

    class Config():
        from_atributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    author_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        from_atributes = True
