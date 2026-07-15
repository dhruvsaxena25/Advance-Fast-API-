from fastapi import FastAPI


# HOW TO INITILIASE FASTAPI APP

app = FastAPI(name= "First APP")

@app.get('/')
def index():
    return {'message': 'Hello, FastAPI'}

