from absl import *
from absn import * 
from absi import *

l = Lancamento ("CREED 3", 10)
print("Diária: R${:.2f}".format(l.r_diaria()))

n = Comum ("Avatar 2" ,7)
print("Diária: R${:.2f}".format(n.r_diaria()))

i = Infantil ("Patas em Furia", 5)
print("Diária: R${:.2f}".format(i.r_diaria()))