from fastapi import FastAPI     # importing FastAPI
import uvicorn

app = FastAPI()                 # creating an instance of FastAPI

@app.get('/')
def index():
    return {'data':{'name':'Shankar'}}

@app.get('/about/')
def about():
    return {'data':{"About page"}}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)

