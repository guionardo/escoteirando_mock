from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Olá mundo: Escoteirando Mockup"

if __name__=='__main__':
    app.run()
