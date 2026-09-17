class Producto:
   def __init__(self, nombre, marca, precio):
       self.nombre = nombre
       self.marca = marca
       self.precio = precio
   def mostrar(self):
       print("Nombre:", self.nombre)
       print("Marca:", self.marca)
       print("Precio: $", self.precio)


productos = []

pila = []

matriz = []
n = int(input("Ingrese el tamaño de la matriz: "))

for i in range(n):
   fila = []
   for j in range(n):
       fila.append(None)
   matriz.append(fila)

while True:
   print("\n===== MENÚ =====")
   print("1. Agregar producto")
   print("2. Mostrar productos")
   print("3. Mostrar productos con precio mayor a $200.000")
   print("4. Agregar producto a la pila")
   print("5. Sacar producto de la pila")
   print("6. Mostrar último producto de la pila")
   print("7. Mostrar matriz")
   print("8. Salir")
   opcion = int(input("Seleccione una opción: "))
   
   if opcion == 1:
       nombre = input("Ingrese el nombre del producto: ")
       marca = input("Ingrese la marca: ")
       precio = float(input("Ingrese el precio: "))
       producto = Producto(nombre, marca, precio)
       productos.append(producto)
       print("Producto agregado correctamente.")
   
   elif opcion == 2:
       if len(productos) == 0:
           print("No hay productos.")
       else:
           for producto in productos:
               producto.mostrar()
               print("----------------")
   
   elif opcion == 3:
       encontrado = False
       for producto in productos:
           if producto.precio > 200000:
               producto.mostrar()
               print("----------------")
               encontrado = True
       if encontrado == False:
           print("No hay productos que superen $200.000.")
  
   elif opcion == 4:
       if len(productos) == 0:
           print("Primero debe agregar productos.")
       else:
           posicion = int(input("Ingrese la posición del producto: "))
           if posicion >= 0 and posicion < len(productos):
               pila.append(productos[posicion])
               print("Producto agregado a la pila.")
           else:
               print("Posicion invalida.")
   
   elif opcion == 5:
       if len(pila) == 0:
           print("La pila esta vacia.")
       else:
           producto = pila.pop()
           print("Producto retirado:")
           producto.mostrar()
   
   elif opcion == 6:
       if len(pila) == 0:
           print("La pila esta vacia.")
       else:
           print("ultimo producto de la pila:")
           pila[-1].mostrar()
  
   elif opcion == 7:
       contador = 0
       for i in range(n):
           for j in range(n):
               if contador < len(productos):
                   matriz[i][j] = productos[contador].nombre
                   contador += 1
       print("\nMATRIZ:")
       for fila in matriz:
           print(fila)
   
   elif opcion == 8:
       print("Programa finalizado.")
       break
   else:
       print("Opcion invalida.")