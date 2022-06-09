from ListaCircular import ListaCircularDE

lista = ListaCircularDE()

lista.agregarInicio(1)
lista.agregarInicio(2)
lista.agregarInicio(3)
lista.agregarInicio(4)
lista.agregarInicio(5)
lista.recorerIF()
print('*' * 25)
print('Número a buscar 3')
print(lista.buscar(3))
