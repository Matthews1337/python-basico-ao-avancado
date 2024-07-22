from models.cliente import Cliente

from models.conta import Conta


matheus = Cliente("Matheus Fonseca", "mat@hotmail.com", "000.000.000-00", "15/10/1997")
macaco = Cliente("Thales Sinhorini", "thales@hotmail.com", "111.111.111-11", "05/03/1999")

print(matheus)

conta_mat = Conta(matheus)
conta_mac = Conta(macaco)

print(conta_mat)
print(conta_mac)