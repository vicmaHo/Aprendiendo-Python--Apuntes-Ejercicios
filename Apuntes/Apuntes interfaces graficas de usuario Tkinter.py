# Apuntes interfaces graficas de usuario
"""
Nos referimos a aplicaciones que presentan una interfz gráfica avanzada
Los elementos basicos son:
Label ---> etiqueta -- mensaje que permite  informale al usuario como interactuar
Button -----> botón -- se asocia para realizar una operacion
Entry ----> Entrada -- se asocia con los datos de entrada y salida


etiquetas(label)
gui: 

LvalorA = Label(gui, text = "valor a")
Lresultado = Label(gui, text = "Resultado")
    nombre                          texto que aparece en la ventana
    
entradas(entryy)
EvalorA = Entry(gui, width = 10)

bitnites(button)
Bboton = Button(gui, text = "boton")

los elementos en Tkinter se colocan de arriba a abajo
con .pack() escribimos los objetos en la  ventana


Para tomar un var que el usuario pone en una entrada usamos
Evalor.get()   ---> .get() nos sirve para obtener el valor
nombre          
de la entrada   

"""