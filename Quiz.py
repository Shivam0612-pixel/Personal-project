import streamlit as st
Score =0
st.write("Q1. What is the first alphabet of english language ?")
st.write(" A) C      B) G      \n C) A      D) F")

Ans = st.text_input("Enter your ans__")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")    
st.write("Q2. Who is known as the Father of the Nation in India?")
st.write("A) Jawaharlal Nehru   B) Subhash Chandra Bose    \nC) Mahatma Gandhi     D) Sardar Patel")
Ans = st.text_input("Enter your ans__")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q3. What is the capital of India?")
st.write("A) Mumbai    B) New Delhi    \nC) Kolkata   D) Chennai")
Ans = st.text_input("Enter your ans__")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q4. Which is the largest planet in our solar system?")
st.write("A) Earth     B) Mars     \nC) Jupiter   D) Saturn")
Ans = st.text_input("Enter your ans__")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q5. Who invented the telephone?")
st.write("A) Thomas Edison    B) Alexander Graham Bell    \nC) Nikola Tesla     D) Newton")
Ans = st.text_input("Enter your ans__")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
if Score == 5:
  st.write('Congrats! you have scored I position in quiz...')
elif Score == 4:
  st.write('Congrats! you have scored II position in quiz...')
else:
  st.write('Better Luck next time...')
