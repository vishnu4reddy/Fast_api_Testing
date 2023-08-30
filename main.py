from fastapi import FastAPI

app = FastAPI()


@app.get("/ \
  'http://127.0.0.1:8000/items/223' \
  -H 'accept: application/json'")
async def read_item(item_id: int):
    return {"item_id": item_id}


# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/223' \
#   -H 'accept: application/json'