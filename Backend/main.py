
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from routes import messages, audio, summary, search

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthcare Translation API")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(messages.router)
app.include_router(audio.router)
app.include_router(summary.router)
app.include_router(search.router)

@app.get("/")
def root():
    return {"status": "API running"}
