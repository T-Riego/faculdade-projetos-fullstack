from imc import calcula_imc, classifica_imc
from tkinter import Button, Tk, Entry , Label , messagebox

def calcular():
    indice = calcula_imc(float(peso.get()), float(altura.get()))
    classificacao = classifica_imc(indice)
    messagebox.showinfo("Classificação", classificacao)

janela = Tk()
peso = Entry(janela)
peso.pack()
altura = Entry(janela)
altura.pack()

botao = Button(janela, text="Clique Aqui", command=saudacao)
botao.pack()

janela.mainloop()