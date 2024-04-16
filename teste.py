from flask import Flask

app = Flask(__name__)

@app.route("/")
def teste():
    return "Testado com sucesso!"