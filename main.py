from fastapi import FastAPI     # importing FastAPI

app = FastAPI()                 # creating an instance of FastAPI

@app.get('/')
def index():
    return {'data':{'name':'Shankar'}}

@app.get('/about/')
def about():
    return {'data':{"About page"}}




