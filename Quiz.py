import streamlit as st


st.write("                    **--  Welcome to first GK Quiz --**    ")
st.write("                      Every Questions contains 5 marks")


score = 0

st.title("Simple Quiz App")

st.write("Q1. What is the first alphabet of english language ?")
st.write("A) C   B) G   C) A   D) F")
Ans = st.text_input("Enter your ans__","Ans 1")

st.write("--------------------------------------------------")

st.write("Q2. Who is known as the Father of the Nation in India?")
st.write("A) Jawaharlal Nehru   B) Subhash Chandra Bose")
st.write("C) Mahatma Gandhi     D) Sardar Patel")
Ans = st.text_input("Enter your ans__","Ans 2")

st.write("--------------------------------------------------")

st.write("Q3. What is the capital of India?")
st.write("A) Mumbai   B) New Delhi   C) Kolkata   D) Chennai")
Ans = st.text_input("Enter your ans__","Ans 3")
st.write("--------------------------------------------------")

st.write("Q4. Which is the largest planet in our solar system?")
st.write("A) Earth   B) Mars   C) Jupiter   D) Saturn")
Ans = st.text_input("Enter your ans__","Ans 4")

st.write("--------------------------------------------------")

st.write("Q5. Who invented the telephone?")
st.write("A) Thomas Edison   B) Alexander Graham Bell")
st.write("C) Nikola Tesla    D) Newton")
Ans = st.text_input("Enter your ans__","Ans 5")

st.write("--------------------------------------------------")
st.write("Q6. Which is the longest river in the world?")
st.write("A) Ganga    B) Amazon    \nC) Nile     D) Yamuna")
Ans = st.text_input("Enter your ans__","Ans 6")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q7. How many states are there in India?")
st.write("A) 28     B) 29    \nC) 30     D) 27")
Ans = st.text_input("Enter your ans__","Ans 7")
if Ans.lower() == "A".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q8. What is the national animal of India?")
st.write("A) Lion      B) Elephant      \nC) Tiger     D) Leopard")
Ans = st.text_input("Enter your ans__","Ans 8")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q9. Which gas do plants absorb from the atmosphere?")
st.write("A) Oxygen       B) Carbon Dioxide    \nC) Nitrogen     D) Hydrogen")
Ans = st.text_input("Enter your ans__","Ans 9")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q10. Who wrote the Indian National Anthem?")
st.write("A) Bankim Chandra Chatterjee     \nB) Rabindranath Tagore      \nC) Sarojini Naidu           \nD) Premchand")
Ans = st.text_input("Enter your ans__","Ans 10")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q11. What is the currency of Japan?")
st.write("A) Dollar    B) Yuan     \nC) Yen       D) Won")
Ans = st.text_input("Enter your ans__","Ans 11")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q12. Which is the smallest continent?")
st.write("A) Europe        B) Australia    \nC) Antarctica    D) South America")
Ans = st.text_input("Enter your ans__","Ans 12")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q13. Who is known as the Missile Man of India?")
st.write("A) APJ Abdul Kalam   B) Vikram Sarabhai      \nC) Homi Bhabha       D) Rakesh Sharma")    
Ans = st.text_input("Enter your ans__","Ans 13")
if Ans.lower() == "A".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q14. What is the chemical symbol of Gold?")
st.write("A) Ag      B) Au     \nC) Fe      D) Cu")
Ans = st.text_input("Enter your ans__","Ans 14")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q15. Which country is known as the Land of Rising Sun?")
st.write("A) China      B) Korea    \nC) Japan      D) Thailand")
Ans = st.text_input("Enter your ans__","Ans 15")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q16. Which is the largest ocean in the world?")
st.write("A) Indian Ocean    B) Atlantic Ocean    \nC) Pacific Ocean   D) Arctic Ocean")
Ans = st.text_input("Enter your ans__","Ans 16")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q17. Who was the first Prime Minister of India?")
st.write("A) Mahatma Gandhi       B) Lal Bahadur Shastri     \nC) Jawaharlal Nehru     D) Indira Gandhi")
Ans = st.text_input("Enter your ans__","Ans 17")
if Ans.lower() == "C".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q18. Which organ purifies blood in the human body?")
st.write("A) Heart     B) Kidney   C) Liver    D) Lungs")
Ans = st.text_input("Enter your ans__","Ans 18")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q19. What is the national sport of India (traditionally considered)?")
st.write("A) Cricket    B) Hockey    \nC) Football   D) Kabaddi")
Ans = st.text_input("Enter your ans__","Ans 19")
if Ans.lower() == "B".lower():
    Score += 5
st.write("---------------------------------------------------------------------------------------------")
st.write("Q20. Which is the tallest mountain in the world?")
st.write("A) K2    B) Kanchenjunga     C) Mount Everest    D) Nanda Devi")
Ans = st.text_input("Enter your ans__","Ans 20")
if Ans.lower() == "C".lower():
    Score += 5 
st.write("---------------------------------------------------------------------------------------------")

# if Score > 30 :
#     st.write("**-** Heartly congratulation to Qualify with ",Score,"/100","**-** ")
# else:
#     st.write("Your Score is",Score,"/100","Not Qualified","\n","Sorry, Better luck for next time")

# if st.button("Submit Quiz"):

#     if ans.lower() == "c":
#         score += 5
#     if ans1.lower() == "c":
#         score += 5
#     if ans2.lower() == "b":
#         score += 5
#     if ans3.lower() == "c":
#         score += 5
#     if ans4.lower() == "b":
#         score += 5

#     st.write("Your Score:", score)

if score >= 90:
    st.success("Congrats! You got 1st position")
    st.balloons()
elif score == 65:
    st.info("Good Job! You got 2nd position")
    st.snow()
else:
    st.error("Better luck next time!")
