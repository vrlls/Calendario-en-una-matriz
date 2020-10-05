#Usted decidió colocar su agenda en una matriz M en la cual los valores filas son los días de la semana y las columnas las horas con solo hora en punto (primera columna = 7, segunda columna = 8 y hace hasta las 12 del medio dia). Usted está ocupado de 7 a 9 todos los días, menos domingo y de 10 a 12 menos los sábados y domingo. Si una persona quiere que le diga si usted está disponible o no a una hora de cierto día la persona debe digitar el día de la semana y la hora en punto en que lo necesita y usted debe retornar "Disponible" o "No disponible" según el caso. Ejemplo: input disponibilidad("Lunes",11) output: "No disponible".
import numpy as np
def disponibilidad(M,dia,hora):
  for i in range(1,8):
    for j in range(1,7):
      if(M[i,0]==dia and M[0,j]==hora):
        return M[i,j]
  return "Fecha no encontrada"



M=[["0","7","8","9","10","11","12"],
  ["lunes", "No disponible", "No disponible", "No disponible", "Disponible", "No disponible", "No disponible"],
  ["martes", "No disponible", "No disponible", "No disponible", "Disponible", "No disponible", "No disponible"],
  ["miercoles", "No disponible", "No disponible", "No disponible", "Disponible", "No disponible", "No disponible"],
  ["jueves", "No disponible", "No disponible", "No disponible", "Disponible", "No disponible", "No disponible"],
  ["viernes", "No disponible", "No disponible", "No disponible", "Disponible", "No disponible", "No disponible"],
  ["sabado", "No disponible", "No disponible", "No disponible", "Disponible","Disponible", "Disponible"],
  ["domingo", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible"]]
M=np.array(M)
dia=str(input())
hora=str(input())
print(disponibilidad(M,dia,hora))




