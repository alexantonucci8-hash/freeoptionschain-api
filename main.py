from fastapi import FastAPI
from freeoptionschain import get_chain

app = FastAPI()

@app.get("/options")
def options(ticker: str = "SPY"):
    return get_chain(ticker)
