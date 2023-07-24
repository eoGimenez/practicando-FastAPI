from fastapi import FastAPI
from routers import blog, user, article
from models.user import Base
from config.db import engine


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(article.router)

Base.metadata.create_all(engine)
