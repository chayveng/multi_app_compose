from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "FastAPI"}

@app.get("/test")
def test():
    return {"messge": "test"}