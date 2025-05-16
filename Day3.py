import streamlit as st

# st.header('st.button')

out = ''
bt_text = 'Say hello'
if st.button(bt_text):
    out = 'Why hello there'
    st.write(out)
    if st.button('Say goodbye'):
        out = 'Goodbye'
        st.write(out)
else:
    out = 'Goodbye'
    st.write(out)
     
