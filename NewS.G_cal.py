cd matplotlib

import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Set page config
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="wide")

# Custom UI Styles using CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f0f5;
    }
    h1 {
        color: #ff7043;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>Scientific Calculator</h1>", unsafe_allow_html=True)

# Choose operation
operation = st.sidebar.selectbox("Select Operation", 
                                 ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 
                                  'Square Root', 'Sine', 'Cosine', 'Tangent', 
                                  'Logarithm', 'Exponential', 'Factorial', 'Plot a Graph'])

# Define operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero" if y == 0 else x / y
def power(x, y): return math.pow(x, y)
def sqrt(x): return math.sqrt(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x, base=10): return math.log(x, base)
def exp(x): return math.exp(x)
def factorial(x): return math.factorial(x)

# Plot graph
def plot_graph(func, start, end):
    x_vals = np.linspace(start, end, 400)
    y_vals = eval(f'np.{func}(np.radians(x_vals))')
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color="#ff7043", linewidth=2.5)
    ax.grid(True)
    st.pyplot(fig)

# Input handling based on operation
if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power']:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    if st.button("Calculate"):
        if operation == 'Add':
            st.success(f"Result: {add(num1, num2)}")
        elif operation == 'Subtract':
            st.success(f"Result: {subtract(num1, num2)}")
        elif operation == 'Multiply':
            st.success(f"Result: {multiply(num1, num2)}")
        elif operation == 'Divide':
            result = divide(num1, num2)
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"Result: {result}")
        elif operation == 'Power':
            st.success(f"Result: {power(num1, num2)}")

elif operation == 'Square Root':
    num = st.number_input("Enter number", value=0.0)
    if st.button("Calculate"):
        st.success(f"Result: {sqrt(num)}")

elif operation in ['Sine', 'Cosine', 'Tangent']:
    angle = st.number_input("Enter angle (degrees)", value=0.0)
    if st.button("Calculate"):
        if operation == 'Sine':
            st.success(f"Result: {sin(angle)}")
        elif operation == 'Cosine':
            st.success(f"Result: {cos(angle)}")
        elif operation == 'Tangent':
            st.success(f"Result: {tan(angle)}")

elif operation == 'Logarithm':
    num = st.number_input("Enter number", value=1.0)
    base = st.number_input("Enter base", value=10.0)
    if st.button("Calculate"):
        st.success(f"Result: {log(num, base)}")

elif operation == 'Exponential':
    num = st.number_input("Enter number", value=0.0)
    if st.button("Calculate"):
        st.success(f"Result: {exp(num)}")

elif operation == 'Factorial':
    num = st.number_input("Enter an integer", value=0, step=1)
    if st.button("Calculate"):
        if num >= 0:
            st.success(f"Result: {factorial(int(num))}")
        else:
            st.error("Error: Factorial of a negative number is undefined.")

elif operation == 'Plot a Graph':
    graph_type = st.selectbox("Choose Function", ['Sine', 'Cosine', 'Tangent'])
    start = st.number_input("Enter start value for X-axis", value=0.0)
    end = st.number_input("Enter end value for X-axis", value=360.0)
    
    if st.button("Plot"):
        plot_graph(graph_type.lower(), start, end)
