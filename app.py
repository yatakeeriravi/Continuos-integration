import streamlit as st
st.title("power calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")
n = st.number_input("Enter an integer", value = 1,step = 1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth_power of {n} is: {fifth_power}")