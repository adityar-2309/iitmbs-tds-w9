import streamlit as st

def find_largest_number(a,b,c):
    return max(a,b,c)

st.title("Find the largest number")
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find the largest number"):
    result = find_largest_number(num1,num2,num3)
    st.write("The largest number is: ", result)
