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
        """Initialize the app with API key and client."""
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
        self.participants = []
        self.scores = {}
        self.custom_dares = []

    def fetch_question(self, question_type: str, intensity: str) -> str:
        """
        Fetch a question from the LLM or fallback.
        """
        try:
            system_instruction = "You are a playful assistant helping with a Truth or Dare game."
            prompt = f"Generate a {intensity} {question_type} question for a fun Truth or Dare game."
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": prompt},
                ],
                model="llama3-8b-8192",
            )
            content = chat_completion.choices[0].message.content.strip()
            return content
        except Exception:
            return None

    def get_question(self, question_type: str, intensity: str) -> str:
        """
        Get a question from the LLM or fallback.
        """
        question = self.fetch_question(question_type, intensity)
        if not question:
            question = random.choice(self.fallback_truths[intensity] if question_type == "truth" else self.fallback_dares[intensity])
        return question

    def add_custom_dare(self, dare: str):
        """
        Add a custom dare to the list.
        """
        self.custom_dares.append(dare)

    def fetch_ai_commentary(self, response: str) -> str:
        """
        Get AI commentary on a truth response.
        """
        try:
            prompt = f"Provide a playful commentary on this response: '{response}'"
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt},
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content.strip()
        except Exception:
            return "That’s an interesting answer! 😉"

    def run(self):
        """
        Main application logic for the Truth or Dare app.
        """
        st.title("Truth or Dare Game 🎭")
        a1, a2 = st.columns([2,1])
        with a1:
            st.write("A fun AI-powered game to spice up your party!")
        with a2:
            # Select intensity level
            intensity = st.radio("Choose Intensity Level:", ["mild", "spicy", "crazy"],  horizontal=True)

        # Input participants
        if "participants" not in st.session_state:
            st.session_state.participants = []

        st.write("### Add Participants")
        participants_input = st.text_area("Enter participant names (one per line):")
        if st.button("Add Participants"):
            participants = participants_input.splitlines()
            st.session_state.participants.extend(participants)
            st.success("Participants added!")

        if st.session_state.participants:
            st.write("### Participants")
            st.write(", ".join(st.session_state.participants))

        

        # Randomly select the next player
        if st.button("Who’s Next?"):
            next_player = random.choice(st.session_state.participants)
            st.write(f"It’s your turn, **{next_player}**!")

            # Truth or Dare selection
            question_type = random.choice(["truth", "dare"])
            question = self.get_question(question_type, intensity)
            st.write(f"**{question_type.capitalize()}:** {question}")

            # Handle responses and commentary for truths
            if question_type == "truth":
                response = st.text_input("Your Answer:")
                if st.button("Submit Answer"):
                    commentary = self.fetch_ai_commentary(response)
                    st.write(f"AI says: {commentary}")

        # # Add custom dares
        # st.write("### Add Custom Dares")
        # custom_dare = st.text_input("Enter a custom dare:")
        # if st.button("Add Dare"):
        #     self.add_custom_dare(custom_dare)
        #     st.success("Custom dare added!")

        # Display a leaderboard
        st.write("### Leaderboard")
        st.write(self.scores if self.scores else "No scores yet. Complete more dares!")

        # Add penalties
        st.write("### Penalty Box")
        penalties = ["Do 10 push-ups", "Sing a song loudly", "Share an embarrassing moment"]
        st.write(f"Suggested Penalty: {random.choice(penalties)}")

        # Save memorable moments
        st.write("### Memorable Moments 📝")
        moment = st.text_input("Write about a funny or memorable moment:")
        if st.button("Save Moment"):
            with open("memorable_moments.txt", "a") as file:
                file.write(f"{moment}\n")
            st.success("Moment saved successfully!")




# Run the app
if __name__ == "__main__":
    app = TruthOrDareApp()
    app.run()
