from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

myapp = FastAPI()

class Blog(BaseModel):
    title:str
    body: str
    published: Optional[bool]

#path parameter
@myapp.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title:{blog.title}"}

if __name__ == '__main__':
    uvicorn.run(myapp,host="127.0.0.1",port=1000)