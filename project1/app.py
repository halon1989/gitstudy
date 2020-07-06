from flask import Flask

app = Flask(__name__)
num2 = 300
num3 = 400

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
