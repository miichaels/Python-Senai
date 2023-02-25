class Pessoa:
    def __init__(self, nome, sexo, cpf, email,ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.email = email
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")

if __name__ == "__main__":
    pessoa1 = Pessoa("Michael", "M", "123.456.789-00", "michael@gmail.com",  True)
    pessoa1.desativar()
