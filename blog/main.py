from fastapi import FastAPI
from . import schemas
app = FastAPI()
    
# class Blog():
#     title: str
#     body: str

@app.post('/blog')
def create(request:schemas.Blog):
    return request
    return 'creating'

# @app.post('/blog')
# def create(title,body):
#     return {'title':title,'body':body}
#     return 'creating'