<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Dockerized Python App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Dockerized Python App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 784e4ad (Initial commit with project files)
