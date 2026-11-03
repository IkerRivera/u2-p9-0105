
import matplotlib.pyplot as plt

# Iker Alexandro Montoya Rivera NC 0105

# Materias
materias = ["Matematicas", "Ingles", "Programacion", "Fisica", "Quimica"]

# Calificaciones
calificaciones = [90, 85, 100, 80, 95]

# Crear grafica de pastel
plt.pie(calificaciones, labels=materias, autopct="%1.1f%%")

# Personalizar grafica
plt.title("Calificaciones NC 0105")
plt.xlabel("Materias")

# Guardar imagen
plt.savefig("grafica_materias_0105.png")

# Mostrar grafica
plt.show()

# Imprimir nombre y numero de control
print("Iker Alexandro Montoya Rivera")
print("NC 0105")
