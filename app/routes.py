from app import app

@app.get('/')
def home():
    return "Hello World"
