# Simple Calculator with Streamlit

import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit app
st.title("Simple Calculator")

# Input for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on operation selected
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")
