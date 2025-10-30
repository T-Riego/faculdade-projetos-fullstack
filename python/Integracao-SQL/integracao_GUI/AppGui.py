import tkinter as tk
from tkinter import ttk, messagebox  # Importando messagebox para feedback
from AppBD import AppBD

class PrincipalBD:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gestão de Produtos")
        self.root.geometry("550x550") # Definindo um tamanho inicial

        # Componentes da interface gráfica
        frame_entradas = tk.Frame(self.root)
        frame_entradas.pack(pady=10)

        self.lblCodigo = tk.Label(frame_entradas, text="Código")
        self.lblCodigo.grid(row=0, column=0, padx=5, pady=5)
        self.txtCodigo = tk.Entry(frame_entradas, state='readonly') # Código não deve ser editável
        self.txtCodigo.grid(row=0, column=1, padx=5, pady=5)

        self.lblNome = tk.Label(frame_entradas, text="Nome")
        self.lblNome.grid(row=1, column=0, padx=5, pady=5)
        self.txtNome = tk.Entry(frame_entradas)
        self.txtNome.grid(row=1, column=1, padx=5, pady=5)

        self.lblPreco = tk.Label(frame_entradas, text="Preço")
        self.lblPreco.grid(row=2, column=0, padx=5, pady=5)
        self.txtPreco = tk.Entry(frame_entradas)
        self.txtPreco.grid(row=2, column=1, padx=5, pady=5)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=10)

        self.btnCadastrar = tk.Button(frame_botoes, text="Cadastrar", command=self.fCadastrarProduto, width=15)
        self.btnCadastrar.grid(row=0, column=0, padx=5)

        self.btnAtualizar = tk.Button(frame_botoes, text="Atualizar", command=self.fAtualizarProduto, width=15)
        self.btnAtualizar.grid(row=0, column=1, padx=5)

        self.btnExcluir = tk.Button(frame_botoes, text="Excluir", command=self.fExcluirProduto, width=15)
        self.btnExcluir.grid(row=0, column=2, padx=5)

        self.btnLimpar = tk.Button(frame_botoes, text="Limpar", command=self.fLimparTela, width=15)
        self.btnLimpar.grid(row=0, column=3, padx=5)

        frame_treeview = tk.Frame(self.root)
        frame_treeview.pack(pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_treeview, columns=("CODIGO", "NOME", "PRECO"), show='headings')
        self.tree.heading("CODIGO", text="Código")
        self.tree.heading("NOME", text="Nome")
        self.tree.heading("PRECO", text="Preço")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind('<ButtonRelease-1>', self.apresentarRegistrosSelecionados)

        self.carregarDadosIniciais()

    ### CORREÇÃO 1: Todos os métodos foram indentados para dentro da classe ###
    def fCadastrarProduto(self):
        nome = self.txtNome.get()
        preco = self.txtPreco.get()

        if not nome or not preco:
            messagebox.showwarning("Aviso", "Nome e Preço são obrigatórios.")
            return
        
        ### CORREÇÃO 4: A função agora recebe o novo registro do BD ###
        novo_produto = self.db.inserir_dados(nome, preco)
        if novo_produto:
            ### CORREÇÃO 4: Insere o registro retornado (com o código correto) na Treeview ###
            self.tree.insert("", "end", values=novo_produto)
            self.fLimparTela()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    ### CORREÇÃO 2: Criação do método fAtualizarProduto ###
    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
            return

        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.atualizar_dados(codigo, nome, preco)
        
        # Recarrega a Treeview para mostrar a alteração
        self.carregarDadosIniciais()
        self.fLimparTela()
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

    ### CORREÇÃO 2: Criação do método fExcluirProduto ###
    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            return

        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este produto?"):
            self.db.excluir_dados(codigo)
            self.carregarDadosIniciais()
            self.fLimparTela()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

    def fLimparTela(self):
        self.txtCodigo.config(state='normal') # Habilita para limpar
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.config(state='readonly') # Desabilita novamente
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)
        self.txtNome.focus_set()

    def apresentarRegistrosSelecionados(self, event):
        # Evita erro se clicar em área vazia
        if not self.tree.selection():
            return

        item_selecionado = self.tree.selection()[0]
        valores = self.tree.item(item_selecionado, "values")
        
        self.fLimparTela()
        
        self.txtCodigo.config(state='normal')
        self.txtCodigo.insert(tk.END, valores[0])
        self.txtCodigo.config(state='readonly')
        
        self.txtNome.insert(tk.END, valores[1])
        self.txtPreco.insert(tk.END, valores[2])

    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

### CORREÇÃO 5: Bloco de execução principal ###
if __name__ == '__main__':
    root = tk.Tk()
    app_db = AppBD()
    app_gui = PrincipalBD(root, app_db)
    root.mainloop()