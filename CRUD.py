import sqlite3

# Conectar ao banco de dados (ou criar, se não existir)
conexao = sqlite3.connect('banco_exemplo.db')
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conexao.commit()

# Função para criar um usuário
def criar_usuario(nome, idade, email):
    try:
        cursor.execute("INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
        conexao.commit()
        print("Usuário criado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já está em uso.")

# Função para ler todos os usuários
def ler_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

# Função para atualizar um usuário
def atualizar_usuario(id, nome=None, idade=None, email=None):
    campos = []
    valores = []
    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if idade:
        campos.append("idade = ?")
        valores.append(idade)
    if email:
        campos.append("email = ?")
        valores.append(email)
    valores.append(id)
    comando = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = ?"
    cursor.execute(comando, valores)
    conexao.commit()
    print("Usuário atualizado com sucesso!")

# Função para deletar um usuário
def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    print("Usuário deletado com sucesso!")

# Demonstração do CRUD
criar_usuario("Alice", 30, "alice@email.com")
criar_usuario("Bob", 25, "bob@email.com")

print("\nUsuários antes da atualização:")
ler_usuarios()

atualizar_usuario(1, nome="Alice Silva", idade=31)

print("\nUsuários depois da atualização:")
ler_usuarios()

deletar_usuario(2)

print("\nUsuários depois da exclusão:")
ler_usuarios()

# Fechar a conexão
conexao.close()
