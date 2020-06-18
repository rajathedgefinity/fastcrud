from fastapi import FastAPI
from app.db.db import metadata, engine, database

from app.core.config import settings

metadata.create_all(engine)


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.get('/')
async def hello():
    return {"Hello": "World!"}


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
