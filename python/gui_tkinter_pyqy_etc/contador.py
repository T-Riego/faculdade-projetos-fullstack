import tkinter as tk

contador = 0

def contador_label(lblRotulo):
    # Esta é a função que será chamada repetidamente
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        
        # O segredo está aqui: apenas agende a próxima chamada.
        # Não chame a função novamente de forma direta.
        lblRotulo.after(1000, funcao_contar)

    # Inicia o contador pela primeira vez.
    # As chamadas seguintes serão feitas pelo .after()
    funcao_contar()

# --- Configuração da janela (sem alterações) ---
janela = tk.Tk()
janela.title("Contagem dos Segundos")

lblRotulo = tk.Label(janela, fg="green", font=("Helvetica", 32))
lblRotulo.pack(pady=20, padx=20)

# Inicia o processo do contador
contador_label(lblRotulo)

btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack(pady=10)

janela.mainloop()