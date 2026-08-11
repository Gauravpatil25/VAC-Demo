import streamlit as st

st.title("CITY HOSPITAL MUMBAI")
name=st.text_input("PATIENT NAME")
address=st.text_input("ADDRESS")
age=st.number_input("AGE,1,100")
adhaar=st.number_input("ADHAAR NUMBER",12000)


#Backend logic

import streamlit as st



if st.button("Sumbit", key="submit2")