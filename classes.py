class teste: #Classe Principal
     def __init__(self, valor): #Método construtor da classe
        self.x = valor #self indica uma referencia para o objeto
        self.y = valor
     def soma(self):
        #total = self.x * self.x * self.x
        total = self.x + self.y
        return "Soma realizada: " +str(total)
calc = teste(6) #instanciando um objeto
c = calc.soma()
print(c)

