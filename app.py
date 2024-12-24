import streamlit as st
import random

# Title
st.title("Rock, Scissors, Paper Game")

# Instructions
st.write("Choose your move and see if you can beat the computer!")

# User's choice
user_choice = st.radio("Select your move:", ["Rock", "Scissors", "Paper"])

# Button to play
if st.button("Play"):
    # Computer's random choice
    computer_choice = random.choice(["Rock", "Scissors", "Paper"])
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win! 🎉"
    else:
        result = "You lose! 😢"

    # Display results
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    st.write(f"**Result:** {result}")
