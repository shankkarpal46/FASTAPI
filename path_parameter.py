from fastapi import FastAPI

myapp = FastAPI()

#path parameter
@myapp.get('/')
def show():
    return {'data':'This is my data.'}

@myapp.get('/about/{id}')
def contact(id:int):
    return {'data':id}

@myapp.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

@myapp.get('/blog/uncomplished')
def uncomplished():
    return {'data':'all uncomplished blogs'}

