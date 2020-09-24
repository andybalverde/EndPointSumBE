from fastapi import FastAPI
app = FastAPI()


@app.get("/items/{item_id1}&{item_id2}")
async def read_item(item_id1: int,item_id2: int):
    return {"item_id1": item_id1, "item_id2": item_id2, "suma": item_id1 + item_id2}
