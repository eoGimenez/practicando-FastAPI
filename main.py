from fastapi import FastAPI
from routers import blog, user
from models.user import Base
from config.db import engine


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(engine)
