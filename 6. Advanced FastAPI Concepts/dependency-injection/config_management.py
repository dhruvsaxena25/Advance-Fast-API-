from fastapi import FastAPI, Depends

app = FastAPI()

class Setting:
    def __init__(self):
        self.api_key = "my_secret"
        self.debug = True
        

def get_settings():
    return Setting()


@app.get('/config')
def get_config(setting: Setting = Depends(get_settings)):
    return {'api_key': setting.api_key}



