import streamlit as st
# from chatbot import chatbot

def generate_response(user_input):
    # resp=chatbot(user_input)
    return f"You said: {user_input}:AAAAAAAAANNNSSSSS"

def main():
    st.title("FitChat")
    conversation_history = []

    input_counter = 0
    end_session = st.button("End Session")
    while end_session !=True:
        user_input = st.text_input(f"You:", key=f"user_input_{input_counter}")
        
        if user_input:
            conversation_history.append(("User", user_input))
            bot_response = generate_response(user_input)
            st.text_area(f"Bot:", value=bot_response, height=100)
            conversation_history.append(("Bot", bot_response))

            if end_session:
                break

            input_counter += 1

    if end_session:
            st.write("Thanks for using fitchat!")
if __name__ == "__main__":
    main()

