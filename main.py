from fastapi import FastAPI
from routers import blog


app = FastAPI()

app.include_router(blog.router)
