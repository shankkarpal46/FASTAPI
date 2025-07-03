from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
    
class Blog():
    title: str
    body: str

@app.post('/blog')
def create(title,body):
    return {'title':title,'body':body}
    return 'creating'