import tkinter
import statistics
import tkinter.messagebox

ventana=tkinter.Tk()
ventana.geometry("300x400")

peticionprimeranota=tkinter.Label(text="Primera nota:")
peticionprimeranota.pack()
primeranota=tkinter.Entry()
primeranota.pack()
peticionsegundanota=tkinter.Label(text="Segunda nota:")
peticionsegundanota.pack()
segundanota=tkinter.Entry()
segundanota.pack()
peticionterceranota=tkinter.Label(text="Tercera nota:")
peticionterceranota.pack()
terceranota=tkinter.Entry()
terceranota.pack()
peticioncuartanota=tkinter.Label(text="Cuarta nota:")
peticioncuartanota.pack()
cuartanota=tkinter.Entry()
cuartanota.pack()
peticionquintanota=tkinter.Label(text="Quinta nota:")
peticionquintanota.pack()
quintanota=tkinter.Entry()
quintanota.pack()

def calcular():
    if primeranota.get()=="" or segundanota.get()=="" or terceranota.get()=="" or cuartanota.get()=="" or quintanota.get()=="":
        tkinter.messagebox.showerror("Alerta", "No has ingresado todas las notas.")
        return
    try:
        numeros=[float(primeranota.get()), float(segundanota.get()), float(terceranota.get()), float(cuartanota.get()), float(quintanota.get())]
        promedio=statistics.mean(numeros)
        mensajedelpromedio.config(text=f"Promedio: {promedio}")
        desviacionestandar=statistics.pstdev(numeros)
        mensajedeladesviacionestandar.config(text=f"Desviación estándar: {desviacionestandar}")
        mayornota=max(numeros)
        mensajedelamayornota.config(text=f"Mayor nota: {mayornota}")
        menornota=min(numeros)
        mensajedelamenornota.config(text=f"Menor nota: {menornota}")
    except:
        tkinter.messagebox.showerror("Alerta", "Has ingresado un dato no numérico.")

espacio=tkinter.Label()
espacio.pack()
mensajeparaoprimir=tkinter.Button(text="Calcular", command=calcular)
mensajeparaoprimir.pack()

espacio=tkinter.Label()
espacio.pack()
mensajedelpromedio=tkinter.Label(text="")
mensajedelpromedio.pack()
mensajedeladesviacionestandar=tkinter.Label(text="")
mensajedeladesviacionestandar.pack()
mensajedelamayornota=tkinter.Label(text="")
mensajedelamayornota.pack()
mensajedelamenornota=tkinter.Label(text="")
mensajedelamenornota.pack()

ventana.mainloop()