from app import app

@app.route('/')
@app.route('/index')
@app.route('/JP2GMD')
def index():
    return "Hello, World!"
