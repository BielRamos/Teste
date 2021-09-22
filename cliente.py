 #Classe do Cliente/método

class Cliente:

    def __init__(self, nome='', rg='', endereco='', bairro='', cidade='', telefone='', email='', id='', ativo= False):
        self._nome = nome
        self._rg = rg
        self._endereco = endereco
        self._bairro = bairro
        self._cidade = cidade
        self._telefone = telefone
        self._email = email
        self._id = id
        self._ativo = ativo

        self._nome = {}
        self._rg = {}
        self._endereco = {}
        self._bairro = {}
        self._cidade = {}
        self._telefone = {}
        self._email = {}
        self._id = {}
        self._ativo = {}


    def getNome(self):
        return self._nome

    def setNome(self,valor):
        self._nome = valor

    def getRg(self):
        return self._rg

    def setRg(self, valor):
        self._rg = valor

    def getEndereco(self):
        return self._endereco

    def setEndereco(self, valor):
        self._endereco = valor

    def getBairro(self):
        return self._bairro

    def setBairro(self, valor):
        self._bairro = valor

    def getCidade(self):
        return self._cidade

    def setCidade(self, valor):
        self._cidade = valor

    def getTelefone(self):
        return self._telefone

    def setTelefone(self, valor):
        self._telefone = valor

    def getEmail(self):
        return self._email

    def setEmail(self, valor):
        self._email = valor

    def getId(self):
        return self._id

    def setId(self, valor):
        self._id = valor

    def ativarCliente(self):
        self._ativo = True

    def desativarCliente(self):
        self._ativo = False

    def inserir(self, id, nome, rg, endereco, bairro, cidade, telefone, email, ativo):
        self._nome.update({id: nome})
        self._rg.update({id: rg})
        self._endereco.update({id: endereco})
        self._bairro.update({id: bairro})
        self._cidade.update({id: cidade})
        self._telefone.update({id: telefone})
        self._email.update({id: email})
        self._id.update({id: id})
        self._ativo.update({id: ativo})

    def lista_clientes(self):
        for id, nome in self._nome.items():
            print('ID:', id)
            print('Nome:', nome)
            print('RG:', self._rg.get(id))
            print('Endereço:', self._endereco.get(id))
            print('Bairro:', self._bairro.get(id))
            print('Cidade:', self._cidade.get(id))
            print('Telefone:', self._telefone.get(id))
            print('Email:', self._email.get(id))


    def deletar_cliente(self, id):
        del self._nome[id]
        del self._rg[id]

