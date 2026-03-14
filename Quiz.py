import streamlit as st


st.write("                    **--  Welcome to first GK Quiz --**    ")
st.write("                      Every Questions contains 5 marks")


Score = 0

st.title("Simple Quiz App")

st.write("Q1. What is the first alphabet of english language ?")
st.write("A) C   B) G   C) A   D) F")
Ans1 = st.text_input("Enter your ans__","Q 1 ")
st.write("--------------------------------------------------")
st.write("Q2. Who is known as the Father of the Nation in India?")
st.write("A) Jawaharlal Nehru   B) Subhash Chandra Bose")
st.write("C) Mahatma Gandhi     D) Sardar Patel")
Ans2 = st.text_input("Enter your ans__","Q 2 ")
st.write("--------------------------------------------------")
st.write("Q3. What is the capital of India?")
st.write("A) Mumbai   B) New Delhi   C) Kolkata   D) Chennai")
Ans3 = st.text_input("Enter your ans__","Q 3 ")
st.write("--------------------------------------------------")
st.write("Q4. Which is the largest planet in our solar system?")
st.write("A) Earth   B) Mars   C) Jupiter   D) Saturn")
Ans4 = st.text_input("Enter your ans__","Q 4 ")
st.write("--------------------------------------------------")
st.write("Q5. Who invented the telephone?")
st.write("A) Thomas Edison   B) Alexander Graham Bell")
st.write("C) Nikola Tesla    D) Newton")
Ans5 = st.text_input("Enter your ans__","Q 5 ")
st.write("--------------------------------------------------")
st.write("Q6. Which is the longest river in the world?")
st.write("A) Ganga    B) Amazon    \nC) Nile     D) Yamuna")
Ans6 = st.text_input("Enter your ans__","Q 6 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q7. How many states are there in India?")
st.write("A) 28     B) 29    \nC) 30     D) 27")
Ans7 = st.text_input("Enter your ans__","Q 7 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q8. What is the national animal of India?")
st.write("A) Lion      B) Elephant      \nC) Tiger     D) Leopard")
Ans8 = st.text_input("Enter your ans__","Q 8 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q9. Which gas do plants absorb from the atmosphere?")
st.write("A) Oxygen       B) Carbon Dioxide    \nC) Nitrogen     D) Hydrogen")
Ans9 = st.text_input("Enter your ans__","Q 9 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q10. Who wrote the Indian National Anthem?")
st.write("A) Bankim Chandra Chatterjee     \nB) Rabindranath Tagore      \nC) Sarojini Naidu           \nD) Premchand")
Ans10 = st.text_input("Enter your ans__","Q 10 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q11. What is the currency of Japan?")
st.write("A) Dollar    B) Yuan     \nC) Yen       D) Won")
Ans11 = st.text_input("Enter your ans__","Q 11 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q12. Which is the smallest continent?")
st.write("A) Europe        B) Australia    \nC) Antarctica    D) South America")
Ans12 = st.text_input("Enter your ans__","Q 12 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q13. Who is known as the Missile Man of India?")
st.write("A) APJ Abdul Kalam   B) Vikram Sarabhai      \nC) Homi Bhabha       D) Rakesh Sharma")    
Ans13 = st.text_input("Enter your ans__","Q 13 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q14. What is the chemical symbol of Gold?")
st.write("A) Ag      B) Au     \nC) Fe      D) Cu")
Ans14 = st.text_input("Enter your ans__","Q 14 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q15. Which country is known as the Land of Rising Sun?")
st.write("A) China      B) Korea    \nC) Japan      D) Thailand")
Ans15 = st.text_input("Enter your ans__","Q 15 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q16. Which is the largest ocean in the world?")
st.write("A) Indian Ocean    B) Atlantic Ocean    \nC) Pacific Ocean   D) Arctic Ocean")
Ans16 = st.text_input("Enter your ans__","Q 16 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q17. Who was the first Prime Minister of India?")
st.write("A) Mahatma Gandhi       B) Lal Bahadur Shastri     \nC) Jawaharlal Nehru     D) Indira Gandhi")
Ans17 = st.text_input("Enter your ans__","Q 17 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q18. Which organ purifies blood in the human body?")
st.write("A) Heart     B) Kidney   C) Liver    D) Lungs")
Ans18 = st.text_input("Enter your ans__","Q 18 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q19. What is the national sport of India (traditionally considered)?")
st.write("A) Cricket    B) Hockey    \nC) Football   D) Kabaddi")
Ans19 = st.text_input("Enter your ans__","Q 19 ")

st.write("---------------------------------------------------------------------------------------------")
st.write("Q20. Which is the tallest mountain in the world?")
st.write("A) K2    B) Kanchenjunga     C) Mount Everest    D) Nanda Devi")
Ans20 = st.text_input("Enter your ans__","Q 20 ")

st.write("---------------------------------------------------------------------------------------------")
if st.button("Submit Quiz"):
    if Ans1.lower() == "c".lower():
        Score += 5
    if Ans2.lower() == "c".lower():
        Score += 5
    if Ans3.lower() == "b".lower():
        Score += 5
    if Ans4.lower() == "c".lower():
        Score += 5
    if Ans5.lower() == "b".lower():
        Score += 5
    if Ans6.lower() == "C".lower():
        Score += 5
    if Ans7.lower() == "A".lower():
        Score += 5
    if Ans8.lower() == "C".lower():
        Score += 5
    if Ans9.lower() == "B".lower():
        Score += 5    
    if Ans10.lower() == "B".lower():
        Score += 5    
    if Ans11.lower() == "C".lower():
        Score += 5
    if Ans12.lower() == "B".lower():
        Score += 5   
    if Ans13.lower() == "A".lower():
        Score += 5
    if Ans14.lower() == "B".lower():
        Score += 5    
    if Ans15.lower() == "C".lower():
        Score += 5
    if Ans16.lower() == "C".lower():
        Score += 5
    if Ans17.lower() == "C".lower():
        Score += 5
    if Ans18.lower() == "B".lower():
        Score += 5
    if Ans19.lower() == "B".lower():
        Score += 5   
    if Ans20.lower() == "C".lower():
        Score += 5     
    st.write("Your Score:", score)

if score >= 90:
    st.success("Congrats! You got 1st position")
    st.balloons()
elif score == 65:
    st.info("Good Job! You got 2nd position")
    st.snow()
else:
    st.error("Better luck next time!")
