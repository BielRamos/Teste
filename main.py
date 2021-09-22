from conexao import criar_conexao,fechar_conexao

def inserir_endereco(con,codigo,cidade,bairro,cep,numero,complemento):
    cursor = con.cursor()
    sql = "INSERT INTO endereco (codigo, cidade, bairro, cep, numero, complemento) values (%s,%s,%s,%s,%s,%s)"
    valores = (codigo,cidade,bairro,cep,numero,complemento)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def deletar_endereco(con,codigo):
    cursor = con.cursor()
    sql = "Delete from endereco where codigo = {}".format(codigo)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar_endereco(con):
    cursor = con.cursor()
    sql = "Select * from endereco"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    for linha in valores_lidos:
        print('--------------------------')
        print("codigo: ", linha[0])
        print("cep: ", linha[1])
        print("bairro: ", linha[2])
        print("numero: ", linha[3])
        print("cidade: ", linha[4])
        print("complemento: ", linha[5])
        print('--------------------------')
    cursor.close()

def inserir_editora(con, codEditora, nome_Gerente, codEditoraEndereco, editoraTelefone):
    cursor = con.cursor()
    sql = "INSERT INTO editora (codEditora, nome_Gerente, codEditoraEndereco, editoraTelefone) values (%s,%s,%s,%s)"
    valores = (codEditora, nome_Gerente, codEditoraEndereco, editoraTelefone)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def deletar_editora(con,codEditora):
    cursor = con.cursor()
    sql = "Delete from editora where codEditora = {}".format(codEditora)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar_editora(con):
    cursor = con.cursor()
    sql = "Select * from editora"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    for linha in valores_lidos:
        print('--------------------------')
        print("codEditora: ", linha[0])
        print("nome_Gerente: ", linha[1])
        print("codEditoraEndereco: ", linha[2])
        print("editoraTelefone: ", linha[3])
        print('--------------------------')
    cursor.close()

def inserir_cliente(con, codCliente, nome, cpf_cnpj, clienteTelefone, codClienteEndereco):
    cursor = con.cursor()
    sql = "INSERT INTO cliente (codCliente, nome, cpf_cnpj, clienteTelefone, codClienteEndereco) values (%s,%s,%s,%s,%s)"
    valores = (codCliente, nome, cpf_cnpj, clienteTelefone, codClienteEndereco)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def deletar_cliente(con,codCliente):
    cursor = con.cursor()
    sql = "Delete from cliente where codCliente = {}".format(codCliente)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar_clientes(con):
    cursor = con.cursor()
    sql = "Select * from cliente"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    for linha in valores_lidos:
        print('--------------------------')
        print("codCliente: ", linha[0])
        print("nome: ", linha[1])
        print("codClienteEndereco: ", linha[2])
        print("CPF/CNPJ: ", linha[3])
        print("clienteTelefone: ", linha[4])
        print('--------------------------')
    cursor.close()

def inserir_livro(con, ISBN, nome_autor, assunto, qtd_estoque, codEditora):
    cursor = con.cursor()
    sql = "INSERT INTO livro (ISBN, nome_autor, assunto, qtd_estoque, codEditora) values (%s,%s,%s,%s,%s)"
    valores = (ISBN, nome_autor, assunto, qtd_estoque, codEditora)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def deletar_livro(con,ISBN):
    cursor = con.cursor()
    sql = "Delete from livro where ISBN = {}".format(ISBN)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar_livros(con):
    cursor = con.cursor()
    sql = "Select * from livro"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    for linha in valores_lidos:
        print('--------------------------')
        print("ISBN: ", linha[0])
        print("nome_autor: ", linha[1])
        print("assunto: ", linha[2])
        print("qtd_estoque: ", linha[3])
        print("codEditora: ", linha[4])
        print('--------------------------')
    cursor.close()

def inserir_compra(con, codCliente, ISBN, data_compra):
    cursor = con.cursor()
    sql = "INSERT INTO compra (codCliente, ISBN, data_compra) values (%s,%s,%s)"
    valores = (codCliente, ISBN, data_compra)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def deletar_compra(con, ISBN):
    cursor = con.cursor()
    sql = "Delete from compra where ISBN = {}".format(ISBN)
    cursor.execute(sql)
    cursor.close()
    con.commit()

def listar_compras(con):
    cursor = con.cursor()
    sql = "Select * from compra"
    cursor.execute(sql)
    valores_lidos = cursor.fetchall()
    for linha in valores_lidos:
        print('--------------------------')
        print("codCliente: ", linha[0])
        print("ISBN: ", linha[1])
        print("data_compra: ", linha[2])
        print('--------------------------')
    cursor.close()

def exibir_menu():

    print('1 - Endereço')
    print('2 - Editora')
    print('3 - Cliente')
    print('4 - Livro')
    print('5 - Compra')
    print('6 - Sair')


def main():
    con = criar_conexao("localhost", "root", "", "livraria")

    print('1 - Endereço')
    print('2 - Editora')
    print('3 - Cliente')
    print('4 - Livro')
    print('5 - Compra')
    print('6 - Sair')

    escolha = input('Selecione a opção desejada:')

    while escolha != '6':
        if escolha == '1':
            print('1 - Cadastrar um endereço')
            print('2 - Apagar um endereço')
            print('3 - Listar os endereços')

            opcao = input('O que deseja fazer?:')
            if opcao == '1':
                codigo = input('Digite o código:')
                cidade = input('Informe a cidade:')
                bairro = input('Digite o bairro:')
                cep = input('Digite o CEP:')
                numero = input('Digite o número da casa:')
                complemento = input('Digite o complemento:')
                inserir_endereco(con, codigo, cidade, bairro, cep, numero, complemento)

                print('O endereco foi cadastrado com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '2':
                codigo = input('Digite o codigo do endereço que deseja excluir:')
                deletar_endereco(con, codigo)

                print('O endereco foi excluído com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '3':
                listar_endereco(con)

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            else:
                print('Selecione a opção corretamente!')


        elif escolha == '2':
            print('1 - Cadastrar uma Editora')
            print('2 - Apagar uma Editora')
            print('3 - Listar Editoras')

            opcao = input('Escolha uma opção:')
            if opcao == '1':
                codEditora = input('Digite o codigo da editora')
                nome_Gerente = input('Digite o nome do gerente:')
                codEditoraEndereco = input('Digite o codigo do endereço:')
                editoraTelefone = input('Digite o telefone da editora:')
                inserir_editora(con, codEditora, nome_Gerente, codEditoraEndereco, editoraTelefone)

                print('A Editora foi cadastrada com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '2':
                codEditora = input('Digite o codigo da editora que deseja excluir:')
                deletar_editora(con, codEditora)

                print('A Editora foi excluída com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '3':
                listar_editora(con)

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            else:
                print('Digite uma das opções corretamente')

        elif escolha == '3':
            print('1 - Cadastrar um Cliente')
            print('2 - Apagar um Cliente')
            print('3 - Listar Clientes')

            opcao = input('Escolha uma opção:')
            if opcao == '1':
                codCliente = input('Digite o codigo do cliente:')
                nome = input('Digite o nome do cliente:')
                cpf_cnpj = input('Informe o seu CPF ou o seu CNPJ:')
                clienteTelefone = input('Digite o telefone do cliente:')
                codClienteEndereco = input('Digite o codigo do endereço do cliente:')
                inserir_cliente(con, codCliente, nome, cpf_cnpj, clienteTelefone, codClienteEndereco)

                print('O Cliente foi cadastrado com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '2':
                codCliente = input('Digite o codigo do cliente que deseja excluir:')
                deletar_cliente(con, codCliente)

                print('O Cliente foi excluído com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '3':
                listar_clientes(con)

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            else:
                print('Digite uma das opções corretamente')

        elif escolha == '4':
            print('1 - Cadastrar um Livro')
            print('2 - Apagar um Livro')
            print('3 - Listar Livro')

            opcao = input('Escolha uma opção:')
            if opcao == '1':
                ISBN = input('Informe o ISBN:')
                nome_autor = input('Informe o nome do autor:')
                assunto = input('Informe o Assunto:')
                qtd_estoque = input('Informe quanto tem em estoque deste livro:')
                codEditora = input('Informe o codigo da editora')
                inserir_livro(con, ISBN, nome_autor, assunto, qtd_estoque, codEditora)

                print('O Livro foi cadastrado com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '2':
                ISBN = input('Informe o ISBN que deseja excluir:')
                deletar_livro(con, ISBN)

                print('O Livro foi excluído com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '3':
                listar_livros(con)

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            else:
                print('Digite uma das opções corretamente!')

        elif escolha == '5':
            print('1 - Cadastrar uma Compra')
            print('2 - Apagar uma compra')
            print('3 - Listar Compras')

            opcao = input('Escolha uma opção:')
            if opcao == '1':
                codCliente = input('Informe o codigo do cliente:')
                ISBN = input('Informe o ISBN desejado:')
                data_compra = input('Informe a data em que foi realizada a compra')
                inserir_compra(con, codCliente, ISBN, data_compra)

                print('A Compra foi cadastrada com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '2':
                ISBN = input('Informe o ISBN:')

                deletar_compra(con, ISBN)

                print('A Compra foi excluída com sucesso!')

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            elif opcao == '3':
                listar_compras(con)

                exibir_menu()

                escolha = input('Selecione a opção desejada:')

            else:
                print('Digite uma opção corretamente!')


    fechar_conexao(con)

main()



