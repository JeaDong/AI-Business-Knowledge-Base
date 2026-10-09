import uvicorn
from backend.settings import PORT

if __name__ == '__main__':
    uvicorn.run('backend.main:app', host='127.0.0.1', port=PORT)
