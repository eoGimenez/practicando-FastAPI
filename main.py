from fastapi import FastAPI, Request
from routers import blog, user, article, product
from models.tables import Base
from config.db import engine
from exceptions.story import StoryException
from fastapi.responses import JSONResponse


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.exception_handler(StoryException)
def story_exception_handlre(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


Base.metadata.create_all(engine)
