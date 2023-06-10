import streamlit as st

st.title('Our streamlite calculator app ')

num1 = st.number_input('Please enter a number',key=1)
num2 = st.number_input('Please enter a number',key=2)

def add_two(num_1,num_2):
    result = num_1 + num_2
    return result

# total = add_two(num1,num2)

if st.button("Calculate the result"):
    total = add_two(num1,num2)
    st.write(f'The result is {total} ')

