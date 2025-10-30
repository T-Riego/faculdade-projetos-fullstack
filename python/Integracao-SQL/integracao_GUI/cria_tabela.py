import psycopg2

# Criar conexão
conexao = psycopg2.connect(
    database="lojadb",
    user="postgres",
    password="senha123",
    host="127.0.0.1",
    port="5432"
)  
print("Conexão com o banco de dados aberta com sucesso!")

# Criar cursor
meu_cursor = conexao.cursor()

if __name__ == "__main__":
    meu_cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    ''')
    conexao.commit()
    print("Tabela criada com sucesso!")
    conexao.close()