from flask import Flask

app = Flask(__name__)

@app.route('/')
def cumprimento():
  boas_vindas = "<h1>Ola, programadores!</h1>"
  link= '<p><a href="/user/Usuario">Clique aqui para ir para a página de usuário</a></p>'
  return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user (nome="Usuario"):
    personalizar = f"<h1>Bem-vindo, {nome}!</h1>"
    instruçao = '<p>Adicione seu nome na URL para uma saudação personalizada.</p>'
    return personalizar + instruçao
  
if __name__ == "__main__":
  app.run(debug=True)