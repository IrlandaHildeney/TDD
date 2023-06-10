'''
Disciplina  - Engenharia de software
Alunos - Irlanda Hildeney
         Hamilton Luis

Implementação do trabalho sobre TDD.
As demais implementações como FastAPI, banco de dados e Pytest
serão adicionadas posteriormente, após houver exito nos testes
'''

class Produto:
    def __init__(self, codigo, nome, descricao):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao

class Produtos:
    def __init__(self):
        self.produtos = []

    def add_produto(self, itens):
        self.produtos.append(itens)

    def del_produto(self, itens):
        self.produtos.remove(itens)

    def listar_produtos(self):
        for itens in self.produtos:
            print(f"Código: {itens.codigo}, Nome: {itens.nome}, Descrição: {itens.descricao}")

    def consultar_produto(self, codigo_produto):
        for itens in self.produtos:
            if itens.codigo == codigo_produto:
                print(f"Código: {itens.codigo}, Nome: {itens.nome}, Descrição: {itens.descricao}")
                break

    def atualizar_produto(self, itens,new_codigo, new_nome, new_descricao):
        itens.codigo = new_codigo
        itens.nome = new_nome
        itens.descricao = new_descricao

       
