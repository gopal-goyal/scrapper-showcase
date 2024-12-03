import streamlit as st
import random
import requests
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TruthOrDareApp:
    def __init__(self):
        """Initialize the bot with API key and client."""
        self.groq_api_key = os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=self.groq_api_key)

        # Fallback questions for offline use
        self.fallback_truths = {
            "mild": ["What’s your favorite movie?", "Do you sing in the shower?"],
            "spicy": ["What’s your biggest regret?", "Have you ever cheated on a test?"],
            "crazy": ["What’s the weirdest rumor you’ve heard about yourself?", "Who’s your secret crush?"],
        }
        self.fallback_dares = {
            "mild": ["Stand on one foot for 30 seconds.", "Imitate a dog for 10 seconds."],
            "spicy": ["Post ‘I love pineapple on pizza’ on social media.", "Do 20 squats in a row."],
            "crazy": ["Call your crush and say something funny.", "Try to balance a book on your head while dancing."],
        }

    def fetch_question(self, question_type: str, intensity: str) -> str:
        """
        Fetch a question from the Groq LLM.
        :param question_type: 'truth' or 'dare'
        :param intensity: 'mild', 'spicy', 'crazy'
        :return: Generated question or None if API fails
        """
        system_instruction = "You have to create a hypothetical environment using your powers"
        prompt = f"Generate a {intensity} {question_type} question for a fun Truth or Dare game."
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt},
            ],
            model="llama3-8b-8192",
        )
        # Extract and return the response content
        return chat_completion.choices[0].message.content.strip()
    
    def get_question(self, question_type: str, intensity: str) -> str:
        """
        Get a question from LLM or fallback.
        :param question_type: 'truth' or 'dare'
        :param intensity: 'mild', 'spicy', 'crazy'
        :return: A question string
        """
        question = self.fetch_question(question_type, intensity)
        if not question:
            question = random.choice(self.fallback_truths[intensity] if question_type == "truth" else self.fallback_dares[intensity])
        return question

    def save_moment(self, moment: str):
        """
        Save a memorable moment to a file.
        :param moment: User-submitted memorable moment
        """
        try:
            with open("memorable_moments.txt", "a") as file:
                file.write(f"{moment}\n")
        except Exception as e:
            st.error(f"Error saving moment: {e}")

    def run(self):
        """
        Main application logic for the Truth or Dare app.
        """
        st.title("Truth or Dare Game 🎭")
        st.write("A fun AI-powered game to spice up your party!")

        # Select intensity level
        intensity = st.radio("Choose Intensity Level:", ["mild", "spicy", "crazy"])

        # Truth Button
        if st.button("Truth"):
            truth_question = self.get_question("truth", intensity)
            st.write(f"**Truth:** {truth_question}")

        # Dare Button
        if st.button("Dare"):
            dare_question = self.get_question("dare", intensity)
            st.write(f"**Dare:** {dare_question}")

        # Save memorable moments
        st.write("### Memorable Moments 📝")
        moment = st.text_input("Write about a funny or memorable moment:")
        if st.button("Save Moment"):
            self.save_moment(moment)
            st.success("Moment saved successfully!")


# Run the app
if __name__ == "__main__":
    app = TruthOrDareApp()
    app.run()
