class Pessoa:
    def __init__(self, nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf



ps= Pessoa("Mike", 25, "123.456.789.52")
print(ps.nome)
print(ps.idade)
print(ps._cpf) 

"""
    publico " " = cpf
    privado "_" = _cpf
    protegido "__" = __cpf
"""