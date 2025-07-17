import streamlit as st
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Calculadora de Pendiente entre Dos Puntos")

st.markdown("""
Esta aplicación calcula la **pendiente (m)** entre dos puntos en el plano cartesiano.

La fórmula utilizada es:  
\\[
m = \\frac{y_2 - y_1}{x_2 - x_1}
\\]
""")

# Entrada de datos
st.subheader("Ingresa las coordenadas de los puntos")

col1, col2 = st.columns(2)

with col1:
    x1 = st.number_input("x₁", value=0.0)
    y1 = st.number_input("y₁", value=0.0)

with col2:
    x2 = st.number_input("x₂", value=1.0)
    y2 = st.number_input("y₂", value=1.0)

# Cálculo de la pendiente
if x2 != x1:
    m = (y2 - y1) / (x2 - x1)
    st.success(f"La pendiente es: **m = {m:.2f}**")
else:
    st.error("La pendiente es indefinida (división por cero).")

# Opción para mostrar el gráfico
if st.checkbox("Mostrar gráfico"):
    fig, ax = plt.subplots()
    ax.plot([x1, x2], [y1, y2], marker='o', color='blue', label='Recta')
    ax.set_title("Gráfico de los puntos y la recta")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt

# Título
st.title("Cálculo de Esfuerzo Normal en una Columna")

st.markdown("""
### Contexto de Ingeniería Civil
Esta app calcula el **esfuerzo normal (σ)** en una columna sometida a una **carga axial P**.  
La fórmula es:

\\[
σ = \\frac{P}{A}
\\]

Donde:
- **P**: Carga axial (en Newtons)
- **A**: Área de la sección transversal (en m²)
""")

# Entradas del usuario
P = st.number_input("Carga axial (P) en N", value=10000.0)
b = st.number_input("Base de la sección (m)", value=0.3)
h = st.number_input("Altura de la sección (m)", value=0.3)

# Cálculo del área y esfuerzo
A = b * h
if A > 0:
    sigma = P / A
    st.success(f"Área de la sección: {A:.4f} m²")
    st.success(f"Esfuerzo normal: σ = {sigma:.2f} Pa")
else:
    st.error("El área debe ser mayor que cero.")

# Mostrar gráfico
if st.checkbox("Mostrar diagrama del esfuerzo"):
    fig, ax = plt.subplots()
    ax.barh(["Sección"], [sigma], color='steelblue')
    ax.set_xlabel("Esfuerzo (Pa)")
    ax.set_title("Diagrama del esfuerzo normal")
    st.pyplot(fig)

