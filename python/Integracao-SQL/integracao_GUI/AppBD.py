import psycopg2
from psycopg2 import Error
from faker import Faker

class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                database="lojadb",
                user="postgres",
                password="senha123",
                host="127.0.0.1",
                port="5432"
            )
            self.cur = self.conn.cursor()
            print("Conexão com o Banco de Dados aberta com sucesso!")
        except (Exception, Error) as error:
            print("Falha ao se conectar ao Banco de Dados:", error)

    ### MELHORIA 1: Método para fechar a conexão ###
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
        print("Conexão com o Banco de Dados fechada com sucesso!")

    def selecionar_dados(self):
        try:
            # Ordenar por código para manter a consistência na exibição
            self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")
            registros = self.cur.fetchall()
            return registros
        except (Exception, Error) as error:
            print("Erro ao selecionar dados:", error)
            return []

    def inserir_dados(self, nome, preco):
        try:
            ### MELHORIA 2: Usando RETURNING * para obter o registro completo inserido ###
            sql = '''INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s) RETURNING *'''
            self.cur.execute(sql, (nome, float(preco))) # Converte preço para float
            novo_produto = self.cur.fetchone()
            self.conn.commit()
            print("Inserção realizada com sucesso!")
            return novo_produto # Retorna a tupla (codigo, nome, preco)
        except (Exception, Error) as error:
            print("Erro ao inserir dados:", error)
            ### MELHORIA 3: Adicionado rollback em caso de erro ###
            self.conn.rollback()
            return None

    def atualizar_dados(self, codigo, nome, preco):
        try:
            sql = '''UPDATE PRODUTO SET NOME = %s, PRECO = %s WHERE CODIGO = %s'''
            self.cur.execute(sql, (nome, float(preco), codigo)) # Converte preço
            self.conn.commit()
            print("Atualização realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados:", error)
            self.conn.rollback()

    def excluir_dados(self, codigo):
        try:
            sql = '''DELETE FROM PRODUTO WHERE CODIGO = %s'''
            self.cur.execute(sql, (codigo,))
            self.conn.commit()
            print("Exclusão realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao excluir dados:", error)
            self.conn.rollback()

# Este bloco é ótimo para popular seu banco de dados para testes.
# Execute `python AppBD.py` diretamente no terminal para rodar este trecho.
if __name__ == "__main__":
    app_bd = AppBD()
    if app_bd.conn: # Só continua se a conexão foi bem-sucedida
        fake = Faker('pt_BR')
        
        print("Populando o banco de dados com 5 registros de teste...")
        for _ in range(5):
            nome = fake.word().capitalize()
            preco = round(fake.random_number(digits=4) / 100, 2)
            app_bd.inserir_dados(nome, preco)
        
        app_bd.close_connection()