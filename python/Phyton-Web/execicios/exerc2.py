from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    boas_vindas = "<h1>Ola programadores</h1>"
    instruçao = '<p>Entre com dois numeros.</p>'
    return boas_vindas + instruçao

@app.route('/somar')
@app.route('/somar/<int:num01>/<int:num02>')
def soma(num01=0, num02=0):
    resultado = float(num01) + float(num02)
    return f"<h1>Resultado da soma: {resultado}</h1>"

if __name__ == "__main__":
  app.run(debug=True) 