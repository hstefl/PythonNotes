from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Custom 6 Flask Application'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
