from fastapi import FastAPI    # importing FastAPI. 
from typing import Optional

app = FastAPI()                 # creating an instance.

@app.get('/')
def show():
    return {'data':"Home Page."}

@app.get('/blog')
def index(limit = 10, published:bool = True, sort: Optional[str] = None):
    if published:
        # to print False value you need to remove default value.
        return {'data': f'{limit} blog from the list and published {published} post.'}
    else:
        return {'data': f'{limit} blog from the list.'}
    
@app.get('/blog/{id}/comments')
def comments(id,limit):
    return {'data':{'1','2'}, 'comment':f"There are {limit} comments."}

# URL is able to easily identify which is query parameter and which is path parameter. 

