from flask import Flask

app = Flask(__name__)
num1 = 100
num2 = 200
num3 = 300
num4 = 400
num5 = 500


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
