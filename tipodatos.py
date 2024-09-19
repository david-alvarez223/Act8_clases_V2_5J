print("Clases V2 Alvarez David")
# zona de clases
class Datos:
    # el constructor
    def __init__(self, estatura, peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} Kg")
    def mi_lista(self):
        lista_canciones=["Hole dwelling","end of a life","odds and ends"]
        print(lista_canciones)
        for lis in lista_canciones:
            print(lis)
    def mi_diccionario(self):
        diccionario_nom={
            "Nombres:": "David Eduardo",
            "Apellidos:": "Alvarez Lujan"
        }
        print(diccionario_nom)
        for x,y in diccionario_nom.items():
            print(x,y)
    def mi_tupla(self):
        tup_comida=("galletas oreo","galletas chocolate chips","pizza","hamburger","ramen","sushi")
        print(tup_comida)
        for comida in tup_comida:
            print(comida)
    x=5
    n="Programacion"
# creacion de objeto
info=Datos(1.75,70.5)

# utilizando objetos
info.mostrar_datos()
print("Lista de canciones Alvarez David")
info.mi_lista()
info.mi_diccionario()
print("Comidas favorita:")
info.mi_tupla()
print(Datos.x,Datos.n)
print(info.estatura)