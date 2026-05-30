import tkinter
import math

ventana1=tkinter.Tk()
ventana1.title("Figuras")
ventana1.geometry("620x200+620+200")

def abrircilindro():
    ventana2=tkinter.Toplevel()
    ventana2.title("Cilindro")
    ventana2.geometry("230x170+290+460")
    label1=tkinter.Label(ventana2, text="Radio (cms):")
    label1.place(x=10, y=10)
    label2=tkinter.Label(ventana2, text="Altura (cms):")
    label2.place(x=10, y=40)
    entry1=tkinter.Entry(ventana2)
    entry1.place(x=90, y=10, width=120)
    entry2=tkinter.Entry(ventana2)
    entry2.place(x=90, y=40, width=120)

    def calcular():
        radio=float(entry1.get())
        altura=float(entry2.get())
        volumen=math.pi*(radio**2)*altura
        label3.config(text=f"Volumen (cm3): {volumen:.2f}")
        superficie=2*math.pi*radio*(radio+altura)
        label4.config(text=f"Superficie (cm2): {superficie:.2f}")

    boton4=tkinter.Button(ventana2, bg="PaleTurquoise1", text="Calcular", command=calcular)
    boton4.place(x=90, y=70, width=120)
    label3=tkinter.Label(ventana2, text="Volumen (cm3):")
    label3.place(x=10, y=110)
    label4=tkinter.Label(ventana2, text="Superficie (cm2):")
    label4.place(x=10, y=140)

def abriresfera():
    ventana3=tkinter.Toplevel()
    ventana3.title("Esfera")
    ventana3.geometry("230x140+550+460")
    label5=tkinter.Label(ventana3, text="Radio (cms):")
    label5.place(x=10, y=10)
    entry3=tkinter.Entry(ventana3)
    entry3.place(x=90, y=10, width=120)

    def calcular():
        radio=float(entry3.get())
        volumen=4/3*math.pi*(radio**3)
        superficie=4*math.pi*(radio**2)
        label6.config(text=f"Volumen (cm3): {volumen:.2f}")
        label7.config(text=f"Superficie (cm2): {superficie:.2f}")

    boton5=tkinter.Button(ventana3, bg="PaleTurquoise1", text="Calcular", command=calcular)
    boton5.place(x=90, y=40, width=120)
    label6=tkinter.Label(ventana3, text="Volumen (cm3):")
    label6.place(x=10, y=80)
    label7=tkinter.Label(ventana3, text="Superficie (cm2):")
    label7.place(x=10, y=110)

def abrirpiramide():
    ventana4=tkinter.Toplevel()
    ventana4.title("Pirámide")
    ventana4.geometry("245x200+810+460")
    label8=tkinter.Label(ventana4, text="Base (cms):")
    label8.place(x=10, y=10)
    label9=tkinter.Label(ventana4, text="Altura (cms):")
    label9.place(x=10, y=40)
    label10=tkinter.Label(ventana4, text="Apotema (cms):")
    label10.place(x=10, y=70)
    entry4=tkinter.Entry(ventana4)
    entry4.place(x=106, y=70, width=120)
    entry5=tkinter.Entry(ventana4)
    entry5.place(x=106, y=10, width=120)
    entry6=tkinter.Entry(ventana4)
    entry6.place(x=106, y=40, width=120)

    def calcular():
        ladodelabase=float(entry5.get())
        altura=float(entry6.get())
        apotema=float(entry4.get())
        volumen=(ladodelabase**2)*altura/3
        superficie=(ladodelabase**2)+4*(ladodelabase*apotema/2)
        label11.config(text=f"Volumen (cm3): {volumen:.2f}")
        label12.config(text=f"Superficie (cm2): {superficie:.2f}")

    boton6=tkinter.Button(ventana4, bg="PaleTurquoise1", text="Calcular", command=calcular)
    boton6.place(x=106, y=100, width=120)
    label11=tkinter.Label(ventana4, text="Volumen (cm3):")
    label11.place(x=10, y=140)
    label12=tkinter.Label(ventana4, text="Superficie (cm2):")
    label12.place(x=10, y=170)

def abrircubo():
    ventana5=tkinter.Toplevel()
    ventana5.title("Cubo")
    ventana5.geometry("222x140+1085+460")
    label13=tkinter.Label(ventana5, text="Base (cms):")
    label13.place(x=10, y=10)
    entry7=tkinter.Entry(ventana5)
    entry7.place(x=82, y=10, width=120)

    def calcular():
        ladodelabase=float(entry7.get())
        volumen=ladodelabase**3
        superficie=6*(ladodelabase**2)
        label14.config(text=f"Volumen (cm3): {volumen:.2f}")
        label15.config(text=f"Superficie (cm2): {superficie:.2f}")

    boton9=tkinter.Button(ventana5, bg="PaleTurquoise1", text="Calcular", command=calcular)
    boton9.place(x=82, y=40, width=120)
    label14=tkinter.Label(ventana5, text="Volumen (cm3):")
    label14.place(x=10, y=80)
    label15=tkinter.Label(ventana5, text="Superficie (cm2):")
    label15.place(x=10, y=110)

def abrirprisma():
    ventana6=tkinter.Toplevel()
    ventana6.title("Prisma")
    ventana6.geometry("230x170+1337+460")
    label16=tkinter.Label(ventana6, text="Base (cms):")
    label16.place(x=10, y=10)
    label17=tkinter.Label(ventana6, text="Altura (cms):")
    label17.place(x=10, y=40)
    entry8=tkinter.Entry(ventana6)
    entry8.place(x=90, y=10, width=120)
    entry9=tkinter.Entry(ventana6)
    entry9.place(x=90, y=40, width=120)

    def calcular():
        ladodelabase=float(entry8.get())
        altura=float(entry9.get())
        volumen=(ladodelabase**2)*altura
        superficie=2*(ladodelabase**2)+4*(ladodelabase*altura)
        label18.config(text=f"Volumen (cm3): {volumen:.2f}")
        label19.config(text=f"Superficie (cm2): {superficie:.2f}")

    boton10=tkinter.Button(ventana6, bg="PaleTurquoise1", text="Calcular", command=calcular)
    boton10.place(x=90, y=70, width=120)
    label18=tkinter.Label(ventana6, text="Volumen (cm3):")
    label18.place(x=10, y=110)
    label19=tkinter.Label(ventana6, text="Superficie (cm2):")
    label19.place(x=10, y=140)

boton1=tkinter.Button(ventana1, bg="PaleTurquoise1", text="Cilindro", command=abrircilindro)
boton1.place(x=20, y=30, width=100)
imagen1=tkinter.PhotoImage(file="cilindro.png")
label20=tkinter.Label(ventana1, image=imagen1)
label20.place(x=38, y=65)

boton2=tkinter.Button(ventana1, bg="PaleTurquoise1", text="Esfera", command=abriresfera)
boton2.place(x=140, y=30, width=100)
imagen2=tkinter.PhotoImage(file="esfera.png")
label21=tkinter.Label(ventana1, image=imagen2)
label21.place(x=151, y=71)

boton3=tkinter.Button(ventana1, bg="PaleTurquoise1", text="Pirámide", command=abrirpiramide)
boton3.place(x=260, y=30, width=100)
imagen3=tkinter.PhotoImage(file="piramide.png")
label22=tkinter.Label(ventana1, image=imagen3)
label22.place(x=265, y=70)

boton7=tkinter.Button(ventana1, bg="PaleTurquoise1", text="Cubo", command=abrircubo)
boton7.place(x=380, y=30, width=100)
imagen4=tkinter.PhotoImage(file="cubo.png")
label23=tkinter.Label(ventana1, image=imagen4)
label23.place(x=402, y=85)

boton8=tkinter.Button(ventana1, bg="PaleTurquoise1", text="Prisma", command=abrirprisma)
boton8.place(x=500, y=30, width=100)
imagen5=tkinter.PhotoImage(file="prisma.png")
label24=tkinter.Label(ventana1, image=imagen5)
label24.place(x=515, y=63)

ventana1.mainloop()