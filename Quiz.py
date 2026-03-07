import streamlit as st

score = 0

st.title("Simple Quiz App")

st.write("Q1. What is the first alphabet of english language ?")
st.write("A) C   B) G   C) A   D) F")
ans = st.text_input("Enter your answer for Q1")

st.write("--------------------------------------------------")

st.write("Q2. Who is known as the Father of the Nation in India?")
st.write("A) Jawaharlal Nehru   B) Subhash Chandra Bose")
st.write("C) Mahatma Gandhi     D) Sardar Patel")
ans1 = st.text_input("Enter your answer for Q2")

st.write("--------------------------------------------------")

st.write("Q3. What is the capital of India?")
st.write("A) Mumbai   B) New Delhi   C) Kolkata   D) Chennai")
ans2 = st.text_input("Enter your answer for Q3")

st.write("--------------------------------------------------")

st.write("Q4. Which is the largest planet in our solar system?")
st.write("A) Earth   B) Mars   C) Jupiter   D) Saturn")
ans3 = st.text_input("Enter your answer for Q4")

st.write("--------------------------------------------------")

st.write("Q5. Who invented the telephone?")
st.write("A) Thomas Edison   B) Alexander Graham Bell")
st.write("C) Nikola Tesla    D) Newton")
ans4 = st.text_input("Enter your answer for Q5")

st.write("--------------------------------------------------")

if st.button("Submit Quiz"):

    if ans.lower() == "c":
        score += 5
    if ans1.lower() == "c":
        score += 5
    if ans2.lower() == "b":
        score += 5
    if ans3.lower() == "c":
        score += 5
    if ans4.lower() == "b":
        score += 5

    st.write("Your Score:", score)

    if score == 25:
        st.success("Congrats! You got 1st position")
        st.balloons()
    elif score >= 15:
        st.info("Good Job! You got 2nd position")
    else:
        st.error("Better luck next time!")
