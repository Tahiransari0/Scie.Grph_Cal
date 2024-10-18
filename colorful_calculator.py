
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Set page config
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="wide")

# Custom CSS for colorful UI
st.markdown("""
    <style>
    body {
        background-color: #f0f0f5;
        color: #4d4d4d;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stTextInput, .stNumberInput {
        border-radius: 5px;
        background-color: #e0f7fa;
        font-weight: bold;
        font-size: 16px;
    }
    .stMarkdown {
        color: #ff7043;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.markdown("<h1 style='text-align: center; color: #ff7043;'>Scientific Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>🧮 A colorful scientific calculator with graphing functionality</p>", unsafe_allow_html=True)

# Define layout
with st.sidebar:
    st.markdown("<h2 style='color: #00796b;'>Choose an Operation</h2>", unsafe_allow_html=True)
    operation = st.selectbox("Select operation", 
                             ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 
                              'Square Root', 'Sine', 'Cosine', 'Tangent', 
                              'Logarithm', 'Exponential', 'Factorial', 'Plot a Graph'])

# Basic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero" if y == 0 else x / y
def power(x, y): return math.pow(x, y)
def sqrt(x): return "Error: Negative number" if x < 0 else math.sqrt(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x, base=10): return math.log(x, base)
def exp(x): return math.exp(x)
def factorial(x): return "Error: Negative number" if x < 0 else math.factorial(x)

# Function to plot graphs
def plot_graph(func_name, start, end):
    x_vals = np.linspace(start, end, 400)
    if func_name == 'sin': y_vals = np.sin(np.radians(x_vals))
    elif func_name == 'cos': y_vals = np.cos(np.radians(x_vals))
    elif func_name == 'tan': y_vals = np.tan(np.radians(x_vals))
    elif func_name == 'custom': y_vals = eval(st.text_input("Enter custom expression in terms of 'x':", "np.sin(x)"))

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color="#ff7043", linewidth=2.5)
    ax.set_facecolor("#e0f7fa")
    ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.6)
    ax.axhline(y=0, color='black',linewidth=1)
    ax.axvline(x=0, color='black',linewidth=1)
    st.pyplot(fig)

# Display inputs and results based on operation
if operation == 'Add' or operation == 'Subtract' or operation == 'Multiply' or operation == 'Divide' or operation == 'Power':
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    if operation == 'Add':
        st.success(f"Result: {add(num1, num2)}")
    elif operation == 'Subtract':
        st.success(f"Result: {subtract(num1, num2)}")
    elif operation == 'Multiply':
        st.success(f"Result: {multiply(num1, num2)}")
    elif operation == 'Divide':
        st.error(f"Result: {divide(num1, num2)}")
    elif operation == 'Power':
        st.success(f"Result: {power(num1, num2)}")

elif operation == 'Square Root':
    num = st.number_input("Enter number:", value=0.0)
    st.success(f"Result: {sqrt(num)}")

elif operation == 'Sine' or operation == 'Cosine' or operation == 'Tangent':
    angle = st.number_input("Enter angle in degrees:", value=0.0)
    if operation == 'Sine': st.success(f"Result: {sin(angle)}")
    elif operation == 'Cosine': st.success(f"Result: {cos(angle)}")
    elif operation == 'Tangent': st.success(f"Result: {tan(angle)}")

elif operation == 'Logarithm':
    num = st.number_input("Enter number:", value=1.0)
    base = st.number_input("Enter base:", value=10.0)
    st.success(f"Result: {log(num, base)}")

elif operation == 'Exponential':
    num = st.number_input("Enter number:", value=0.0)
    st.success(f"Result: {exp(num)}")

elif operation == 'Factorial':
    num = st.number_input("Enter an integer:", value=0, step=1)
    st.success(f"Result: {factorial(int(num))}")

elif operation == 'Plot a Graph':
    graph_choice = st.selectbox("Function to plot", ['Sine', 'Cosine', 'Tangent', 'Custom Function'])
    start = st.number_input("Enter start value for X-axis:", value=0.0)
    end = st.number_input("Enter end value for X-axis:", value=360.0)
    
    if graph_choice == 'Sine': plot_graph('sin', start, end)
    elif graph_choice == 'Cosine': plot_graph('cos', start, end)
    elif graph_choice == 'Tangent': plot_graph('tan', start, end)
    elif graph_choice == 'Custom Function': plot_graph('custom', start, end)
