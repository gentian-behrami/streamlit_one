import streamlit as st

st.title('Our streamlite calculator app ')

num1 = st.number_input('Please enter a number',key=1)
num2 = st.number_input('Please enter a number',key=2)

def add_two(num_1,num_2):
    result = num_1 + num_2
    return result

def min_two(num_1,num_2):
    result = num_1 - num_2
    return result

def mul_two(num_1,num_2):
    result = num_1 * num_2
    return result

def div_two(num_1,num_2):
    result = num_1 / num_2
    return result
# total = add_two(num1,num2)

if st.button("Calculate sum of numbers"):
    total = add_two(num1,num2)
    st.write(f'The result is {total} ')
elif st.button("Calculate substraction of numbers"):
    total = min_two(num1,num2)
    st.write(f'The result is {total}')
elif st.button("Calculate multiply of numbers"):
    total = mul_two(num1,num2)
    st.write(f'The result is {total}')
elif st.button("Calculate division of numbers"):
    if num2 == 0:
        st.write('Cannot divide by zero')
    else:
        total = div_two(num1,num2)
        st.write(f'The result is {total}')


