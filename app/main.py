from fastapi import FastAPI, Query
import os
import uvicorn
from finder import FinderModel
import json as json_lib


app = FastAPI()
app.predictor = FinderModel()

@app.get("/hello")
def read_hello():
    return {"message": "hello world"}

@app.get("/predict")
def predict(X: str = Query(..., description="Input text for prediction")):
    json_str  = app.predictor.predict(X)
    json_data = json_lib.loads(json_str)
    results = {'results': json_data, 'message': 'OK'}
    
    
    return results

# @app.get("/query")
# def query_route(query: str = Query(..., description="Search query")):
#     # TODO: write your code here, keeping the return format
#     return {"results": [   {'title':'Document title',
#         'content':'Document content (perhaps only the first 500 words?',
#         'relevance': 0.3
#         },
#         {'title':'Document title',
#         'content':'Document content (perhaps only the first 500 words?',
#         'relevance': 0.2
#         },
#         {'title':'Document title',
#         'content':'Document content (perhaps only the first 500 words?',
#         'relevance': 0.1
#         }
#     ], "message": "OK"}

def run():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()