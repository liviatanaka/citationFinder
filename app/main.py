from fastapi import FastAPI, Query, Response
import os
import uvicorn
from .finder import FinderModel
import json as json_lib


app = FastAPI()
app.predictor = FinderModel()

@app.get("/hello")
def read_hello():
    return {"message": "hello world"}

@app.get("/query")
def query(query: str = Query(..., description="Input text for prediction")):
    json_str  = app.predictor.predict(query)
    json_data = json_lib.loads(json_str)
    results = {'results': json_data, 'message': 'OK'}
    
    pretty_data = json_lib.dumps(results, indent=4)
    return Response(pretty_data, media_type="application/json")


def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()