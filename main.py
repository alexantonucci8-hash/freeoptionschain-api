from fastapi import FastAPI
from freeoptionschain import options_chain

app = FastAPI()

@app.get("/options")
def get_options(ticker: str = "SPY"):
    df = options_chain(ticker=ticker)
    calls = df[df["Type"] == "Call"].to_dict(orient="records")
    return {"calls": calls}
