class PessoaAut: #Classe Principal
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
class PessoaAutenticavel(PessoaAut): #Classe filha
    def __init__(self, nome, sobrenome, idade, usuario, senha):
        PessoaAut.__init__(self, nome, sobrenome, idade)
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha
    
p = PessoaAutenticavel("Michael", "Silva", 25, "sp", "sabao")

print(PessoaAut.nome_completo(p))
print(PessoaAutenticavel.autenticar(p, "sp", "sabao"))