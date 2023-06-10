import mysql.connector

from Connection import Connection

class ProdutoDAO:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Produtos'
        )
        self.mycursor = self.mydb.cursor()
        self.create_table()

    def create_table(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS produtos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")

    def adicionar_produto(self, nome):
        sql = "INSERT INTO produtos (nome) VALUES (%s)"
        values = (nome,)
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print("Produto adicionado com sucesso!")

    def deletar_produto(self, id_produto):
        sql = "DELETE FROM produtos WHERE id = %s"
        values = (id_produto,)
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print("Produto deletado com sucesso!")

    def atualizar_produto(self, id_produto, novo_nome):
        sql = "UPDATE produtos SET nome = %s WHERE id = %s"
        values = (novo_nome, id_produto)
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print("Produto atualizado com sucesso!")

    def listar_produtos(self):
        self.mycursor.execute("SELECT * FROM produtos")
        produtos = self.mycursor.fetchall()
        print("Lista de Produtos:")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}")

    def consultar_produto(self, id_produto):
        sql = "SELECT * FROM produtos WHERE id = %s"
        values = (id_produto,)
        self.mycursor.execute(sql, values)
        produto = self.mycursor.fetchone()
        if produto:
            print(f"ID: {produto[0]}, Nome: {produto[1]}")
        else:
            print("Produto não encontrado.")

# Função para exibir o menu de opções para o usuário
def exibir_menu():
    print("===== Menu de Opções =====")
    print("1. Adicionar Produto")
    print("2. Deletar Produto")
    print("3. Atualizar Produto")
    print("4. Listar Produtos")
    print("5. Consultar Produto")
    print("0. Sair")
    print("==========================")

def main():
    minha_conexao = Connection(host="localhost", user="root", password="")
    produto_dao = ProdutoDAO()
   
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            produto_dao.adicionar_produto(nome)
        elif opcao == "2":
            id_produto = input("Digite o ID do produto a ser deletado: ")
            produto_dao.deletar_produto(id_produto)
        elif opcao == "3":
            id_produto = input("Digite o ID do produto a ser atualizado: ")
            novo_nome = input("Digite o novo nome do produto: ")
            produto_dao.atualizar_produto(id_produto, novo_nome)
        elif opcao == "4":
            produto_dao.listar_produtos()
        elif opcao == "5":
            id_produto = input("Digite o ID do produto a ser consultado: ")
            produto_dao.consultar_produto(id_produto)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()