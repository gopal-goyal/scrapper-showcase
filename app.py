import streamlit as st

# Set the title of the dashboard
st.title("Scrapper's Showcase")

# About Me section
st.header("About Me")
st.write("""
I'm Scrapper, a solo and slow developer who likes to build anything and everything and I don't even know why!
If you wanna know something then feel free to explore here. Any feedback would be most welcome.
If you like my work consider buying me a muffin and a coffee ☕️ :).
""")

# Projects section
st.header("Projects")
projects = {
    "Thought Session Bot": "A go to chatbot for just putting out random thoughts with the ability for thought provoking answers!",
    "Truth or Dare": "Integrated with the power of AI, this game takes turn you would never expect!",
    "Project 3": "Still in Dev bro!"
}

for project, description in projects.items():
    st.subheader(project)
    st.write(description)
    if project=="Thought Session Bot":
        st.page_link("pages/chatbot.py", label="View Thought Session Bot", icon="🤖")
    if project=="Truth or Dare":
        st.page_link("pages/truth_or_dare.py", label="Play the Game!", icon="🀄️")

# # Technologies Used section
# st.header("Technologies Used")
# technologies = [
#     "Frontend: React, HTML, CSS, Streamlit, Django",
#     "Backend: Node.js, Express, python",
#     "Data Analysis: Python, Pandas, Streamlit",
#     "Machine Learning: Scikit-learn, TensorFlow",
#     "Tools & Platforms: Git, GitHub, AWS, Docker"
# ]
# for tech in technologies:
#     st.write(f"- {tech}")

# Contact section
st.header("Contact")
st.write("I’d love to connect with you! Feel free to reach out via:")
st.write("- **Email**: goyal11.gopal@gmail.com")
st.write("- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/gopal911/)")
st.write("- **GitHub**: [Your GitHub Profile](https://github.com/gopal-goyal)")

# Run the app
if __name__ == "__main__":
    st.sidebar.title("Faltu Bakwaaas!")
    st.sidebar.markdown("Idhar to kuch bhi likhdo kon hi padhta hai")

