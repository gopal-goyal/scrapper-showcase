import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ThoughtSessionBot:
    def __init__(self):
        """Initialize the bot with API key and client."""
        self.groq_api_key = os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=self.groq_api_key)

    def call_groq(self, user_prompt):
        """
        Call the Groq LLM API with a modified prompt to generate a 
        crisp and thought-provoking response.
        """
        # Modify the prompt to guide the LLM
        system_instruction = (
            "You will never give straight replies. You are very irritating model."
        )
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt},
            ],
            model="llama3-8b-8192",
        )
        # Extract and return the response content
        return chat_completion.choices[0].message.content.strip()

    def chatbot_ui(self):
        """Render the Streamlit UI for the chatbot."""
        st.title("Thought Session Bot")
        st.divider()

        # Create a container for chat messages with scrollable content
        with st.container():
            # Display previous messages if available
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Create a scrollable container for the messages
            chat_container = st.container()

            # Display previous chat messages
            with chat_container:
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        st.write(f"**You:** {msg['content']}")
                    else:
                        st.write(f"**Bot:** {msg['content']}")

        # Form for input box and button
        with st.form(key="input_form", clear_on_submit=True):
            # Input box at the bottom
            user_prompt = st.text_area("Enter your thought here!", key="user_input", height=100)
            submit_button = st.form_submit_button("Generate a response thought!")
            
            if submit_button:
                if user_prompt.strip():
                    try:
                        # Add user's message to session state
                        st.session_state.messages.append({"role": "user", "content": user_prompt})
                        # Get bot response
                        content = self.call_groq(user_prompt)
                        # Add bot's message to session state
                        st.session_state.messages.append({"role": "bot", "content": content})
                    except Exception as e:
                        st.error("Error generating response. Please try again later.")
                        st.write(f"Details: {e}")
                else:
                    st.warning("Please enter a thought to receive a response.")
        
        # Use custom CSS for the scrollable chat box
        st.markdown(
            """
            <style>
                /* Styling for the chat container */
                .streamlit-expanderHeader {
                    background-color: transparent;
                }

                /* Styling for the chat messages container */
                .stContainer {
                    height: 400px;
                    overflow-y: auto;
                }

                /* Styling for the input area and button */
                .stTextArea textarea {
                    width: 100%;
                    margin-bottom: 10px;
                }
                .stButton button {
                    width: 100%;
                }
                .stForm {
                    margin-top: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Entry point
if __name__ == "__main__":
    bot = ThoughtSessionBot()
    bot.chatbot_ui()
