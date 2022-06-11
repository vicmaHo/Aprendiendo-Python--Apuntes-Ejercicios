# creacion de archivos
nombre = "Nombre.py"
archivo = open(nombre, "w") # w --> crea / borra el arhivo para escritura
                            # r -> abre para solo lectura
                            # a -> crea/ agrega al final dela archivo

archivo.write("print(\"Hola mundo\"")
archivo.write("\n")

archivo.close() # Es importante cerrar el archivo para que no se corrompa

# leer el archivo

# imprimir en un archivo
print("Holaaa", file=archivo) # file esta por defecto para imprimir en consola, si caambiamos el para
                                # metro
                                

# ñeer archivos con with