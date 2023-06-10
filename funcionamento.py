
from produto import Produtos, Produto


def exibir_menu():
    print("\n====== Menu ========")
    print("[1] Adicionar Produto")
    print("[2] Deletar Produto")
    print("[3] Listar Produtos")
    print("[4] Consultar Produto")
    print("[5] Atualizar Produto")
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
        codigo = input("\nDigite o codigo do produto: ")
        if not is_numero(codigo):
            print("Código invalido, Digite apenas números")
            continue
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        itens = Produto(codigo, nome, descricao)
        system.add_produto(itens)
        print("==============================\nProduto adicionado com sucesso!\n==============================\n")

    elif op == "2":
        codigo = input("\nDigite o codigo do produto que deseja deletar: ")
        if not is_numero(codigo):
            print("Código invalido, Digite apenas números")
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
            print("Código invalido, Digite apenas números")
            continue
        system.consultar_produto(codigo)

    elif op == "5":

        codigo = input("\nDigite o código do produto que deseja atualizar: ")
        if not is_numero(codigo):
            print("Código invalido, Digite apenas números")
            continue
        produto_encontrado = False

        for itens in system.produtos:

            if itens.codigo == codigo:
                new_codigo = input("\nDigite o novo codigo do produto: ")
                if not is_numero(new_codigo):
                    print("Código invalido, Digite apenas números")
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
