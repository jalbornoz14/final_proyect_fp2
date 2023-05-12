from tkinter import *
ventana = Tk()


ventana.geometry("600x400")

ventana.title("Ingreso al sistema de Vacunacion 360")


boton_ingresar = Button(ventana, width=10, text="Ingresar", fg="blue")
boton_ingresar.place(x=150, y=350)

boton_salida = Button(ventana, width=10, text="Salir", fg="blue", command=ventana.quit)
boton_salida.place(x=300, y=350)


usuario_label = Label(ventana, text="Ingrese su usuario")
usuario_label.place(x=200, y=50)
usuario_caja_texto = Entry(ventana)
usuario_caja_texto.place(x=330, y=50)

password_label = Label(ventana, text="Ingrese su password").place(x=200, y=80)
password_caja_texto = Entry(ventana).place(x=330, y=80)

ventana.mainloop()