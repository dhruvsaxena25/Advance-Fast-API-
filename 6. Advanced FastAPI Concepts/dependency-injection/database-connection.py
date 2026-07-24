from fastapi import FastAPI, Depends

app = FastAPI()

class MockDB:
    def __init__(self):
        self.conncection = 'mock_db_conncection'
    def close(self):
        print('Mock DB Closed')

# Dependency Function

def get_db():
    db = MockDB()
    
    try:
        yield db
    finally:
        db.close()
        
@app.get('/home')
def home(db: MockDB = Depends(get_db)):
    return {'db_Status':    db.conncection}