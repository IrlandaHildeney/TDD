from produto import Produtos, Produto


def exibir_menu():
    print("\n====== Menu ========")
    print("[1] Adicionar produto")
    print("[2] Deletar produto")
    print("[3] Listar todos os produtos")
    print("[4] Consultar um produto")
    print("[5] Atualizar produto")
    print("[0] Sair")


#Para ler a opção do usuário
def ler_opcao():
    op = input("Escolha uma opção: ")
    return op


system = Produtos()

#Usuario nao digitar letras no campo "código"
def is_numero(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


while True:
    exibir_menu()
    op = ler_opcao()

    if op == "1":
        codigo = input("\nDigite o código do produto: ")
        if not is_numero(codigo):
            print("Código inválido! Digite apenas números...")
            continue
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        itens = Produto(codigo, nome, descricao)
        system.add_produto(itens)
        print("==============================\nProduto adicionado com sucesso!\n==============================\n")

    elif op == "2":
        codigo = input("\nDigite o codigo do produto que deseja deletar: ")
        if not is_numero(codigo):
            print("Código inválido! Digite apenas números...")
            continue
        produto_encontrado = False

        for itens in system.produtos:
             if itens.codigo == codigo:
                system.del_produto(itens)
                print("==============================\nProduto deletado com sucesso!\n==============================\n")
                produto_encontrado = True

        if not produto_encontrado:
            print("Produto não encontrado!")

    elif op == "3":
        print("==========================\n")
        system.listar_produtos()

    elif op == "4":

        codigo = input("\nDigite o código do produto que deseja consultar: ")
        if not is_numero(codigo):
            print("Código inválido, Digite apenas números")
            continue
        system.consultar_produto(codigo)

    elif op == "5":

        codigo = input("\nDigite o código do produto que deseja atualizar: ")
        if not is_numero(codigo):
            print("Código inválido, Digite apenas números")
            continue
        produto_encontrado = False

        for itens in system.produtos:

            if itens.codigo == codigo:
                new_codigo = input("\nDigite o novo código do produto: ")
                if not is_numero(new_codigo):
                    print("Código inválido, Digite apenas números")
                    continue
                new_nome = input("Digite o novo nome do produto: ")
                new_descricao = input("Digite a nova descrição do produto: ")

                system.atualizar_produto(itens, new_codigo, new_nome, new_descricao)
                print('==============================\nProduto atualizado com sucesso!\n==============================\n')
                produto_encontrado = True

        if not produto_encontrado:
            print("Produto não encontrado!")


    elif op == "0":
        print("==============================\nOperação encerrada!\n==============================\n")
        break

    else:
        print("Opção inválida")

from produto import Produtos, Produto
from pytest import *

# Teste para a função is_numero
def test_is_numero():
    assert is_numero("123") == True
    assert is_numero("abc") == False

# Teste para adicionar um produto
def test_adicionar_produto():
    system = Produtos()
    produto = Produto("1", "Produto A", "Descrição do Produto A")
    system.add_produto(produto)
    assert len(system.produtos) == 1

# Teste para deletar um produto
def test_deletar_produto():
    system = Produtos()
    produto = Produto("1", "Produto A", "Descrição do Produto A")
    system.add_produto(produto)
    system.del_produto(produto)
    assert len(system.produtos) == 0

# Teste para consultar um produto
def test_consultar_produto():
    system = Produtos()
    produto = Produto("1", "Produto A", "Descrição do Produto A")
    system.add_produto(produto)
    assert system.consultar_produto("1") == produto

# Teste para atualizar um produto
def test_atualizar_produto():
    system = Produtos()
    produto = Produto("1", "Produto A", "Descrição do Produto A")
    system.add_produto(produto)
    new_codigo = "2"
    new_nome = "Produto B"
    new_descricao = "Descrição do Produto B"
    system.atualizar_produto(produto, new_codigo, new_nome, new_descricao)
    assert produto.codigo == new_codigo
    assert produto.nome == new_nome
    assert produto.descricao == new_descricao

# Executar os testes
if __name__ == '__main__':
    pytest.main()
