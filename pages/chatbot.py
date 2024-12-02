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
            "You are a creative and reflective assistant. Your task is to transform "
            "the user's input into a single, impactful, and thought-provoking statement. "
            "The response should be catchy, easy to read, and never more than one sentence."
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
        user_prompt = st.text_area("Enter your thought here!")
        if st.button("Generate a response thought!"):
            st.divider()
            if user_prompt.strip():
                try:
                    content = self.call_groq(user_prompt)
                    st.write(content)
                except Exception as e:
                    st.error("Error generating response. Please try again later.")
                    st.write(f"Details: {e}")
            else:
                st.warning("Please enter a thought to receive a response.")

# Entry point
if __name__ == "__main__":
    bot = ThoughtSessionBot()
    bot.chatbot_ui()
