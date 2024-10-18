import streamlit as st

# Set the title of the dashboard
st.title("Scrapper's Showcase")

# About Me section
st.header("About Me")
st.write("""
I'm Scrapper, a passionate developer with a keen interest in creating innovative solutions. 
I enjoy tackling complex challenges and continuously learning new technologies. 
My goal is to build impactful software that enhances user experiences and drives efficiency.
""")

# Technologies Used section
st.header("Technologies Used")
technologies = [
    "Frontend: React, HTML, CSS, JavaScript",
    "Backend: Node.js, Express",
    "Data Analysis: Python, Pandas, Streamlit",
    "Machine Learning: Scikit-learn, TensorFlow",
    "Tools & Platforms: Git, GitHub, AWS, Docker"
]
for tech in technologies:
    st.write(f"- {tech}")

# Projects section
st.header("Projects")
projects = {
    "Project Name 1": "Brief description of the project, its purpose, and any notable features.",
    "Project Name 2": "Brief description of the project, its purpose, and any notable features.",
    "Project Name 3": "Brief description of the project, its purpose, and any notable features."
}

for project, description in projects.items():
    st.subheader(project)
    st.write(description)

# Contact section
st.header("Contact")
st.write("I’d love to connect with you! Feel free to reach out via:")
st.write("- **Email**: your-email@example.com")
st.write("- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
st.write("- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)")

# Run the app
if __name__ == "__main__":
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Use the sidebar to navigate through the sections.")

