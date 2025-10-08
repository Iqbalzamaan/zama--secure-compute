import streamlit as st

st.title("Zama Secure Compute Demo")
st.write("Printing numbers 1 to 25:")
for i in range(1, 26):
    st.write(i)

st.write("Hello World 5 times:")
for i in range(5):
    st.write([f"Hello World {i+1}" for i in range(5)])
