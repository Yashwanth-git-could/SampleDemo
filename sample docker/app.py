from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    a=8
    b=6
    return a-b

@app.get("/health")
def health_check():
    return {"status": "healthy"}
2
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}