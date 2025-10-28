from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Pagina principal</h1>" 

@app.route("/ola/")
@app.route("/ola/<nome>")
def ola(nome=None):
  if nome:
    return f"<h1>Ola, {nome}!</h1>"
  return "<h1>Ola, mundo!</h1>"

if __name__ == "__main__":
  app.run() 
