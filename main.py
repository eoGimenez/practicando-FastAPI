from fastapi import FastAPI, Request
from routers import blog, user, article, product
from auth import authentication
from models.tables import Base
from config.db import engine
from exceptions.story import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)


@app.exception_handler(StoryException)
def story_exception_handlre(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


Base.metadata.create_all(engine)
