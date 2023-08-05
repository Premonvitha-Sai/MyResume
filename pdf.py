import streamlit as st

def main():
    st.markdown(
        r"""
        <style>
        .reportview-container {
            background: url('background.jpg') no-repeat center fixed;
            background-size: cover;
        }
        h1 {
            color: yellow;
        }
        h2 {
            color: yellow;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Resume"])

    if page == "Homepage":
        st.header("This is Rayana Premonvitha Sai' Resume ")
        
        st.image('c.gif')

    elif page == "Resume":
        st.title("Rayana Premonvitha Sai's Resume")
        
        st.header("Personal Information")
        st.write("Visakhapatnam, Andhra Pradesh, India")
        st.write("Mobile : +918790087950")
        st.write("Email : monvithasai.rayana@gmail.com")
        st.write("Age/Gender : 20, Female")
        st.write("Github : [Link](https://github.com/Premonvitha-Sai)")

        st.header("Education")
        st.write("B. Tech., Computer Science Engineering, Gayatri Vidya Parishad College of Engineering For Women")
        st.write("Board: Jawaharlal Nehru Technological University")
        st.write("Marks: 74.40")
        st.write("12th - BIEAP - 90.92")
        st.write("10th - SSC - 92.15")

        st.header("Skills")
        st.write("""
        - Programming Languages: C, Java, JavaScript, PHP, Python, HTML, XML
        - Database: Oracle, MySQL, MongoDB
        - Operating Systems: Windows 10, Windows XP/Vista/7
        - Certifications: Machine learning, Artificial Intelligence, Deep Learning
        - Software: Jupyter notebook, Google Colab, Visual Studio, Python IDE, Mathematica, MS Word, MS Excel, MS PowerPoint
        - Other Skills: ML, AI, Computer vision, Data analysis, Web development, NLP, CSS
        - Mobile Development: Android
        """)

        st.header("Projects")
        st.subheader("Electric Vehicle Market Segmentation - Feynn Labs")
        st.write("Oct, 2022 - Dec, 2022")
        st.write("Details: The Electric Vehicle Market Segmentation project employs data analysis and machine learning techniques to examine the growth of the electric vehicle industry on a daily basis...")

        st.subheader("Road Lane Detection - Code Clause")
        st.write("Nov, 2021 - Dec, 2021")
        st.write("Details: Developing a road lane detection project using AI involves steps such as data collection, preprocessing, training the AI model...")

        st.subheader("Spam Email Detection using streamlit - Oasis Infobyte")
        st.write("Details: The Spam Email Detection project utilizes Streamlit and machine learning algorithms to create a web application capable of identifying and filtering out spam emails...")

        st.subheader("PNEUMONIA Detection Using Deep Learning")
        st.write("Details: This project aims to develop a pneumonia detection system using deep learning techniques in TensorFlow, Keras, and Python...")

        st.subheader("Emotion Detection using OpenCV & Python")
        st.write("Details: This project aims to develop an emotion detection system using OpenCV and Python, employing deep learning techniques...")

        st.header("Project Links")
        st.markdown("[MNIST Model App](https://accuracymnist-fltryjbc5oi.streamlit.app/)")
        st.markdown("[Job Recommendation App](https://examapp.streamlit.app/)")
        st.markdown("[Job Search App](https://jobapp.streamlit.app/)")
        st.markdown("[Handwritten Digit Classification App](https://mnistcnn-7y5tfkyaefue65vgdkve5d.streamlit.app/)")
        st.markdown("[Handwritten Digit Classification App using MLP](https://mnistmlp.streamlit.app/)")

        st.header("Academics and Certifications")
        st.write("""
        - Certified by Infosys spring board in HTML, CSS, Javascript.
        - Achieved 95% in the International Math Olympiad (IMO) with a state rank of 363 and an international rank of 571.
        - Secured 92.3% in JEE Main examination.
        - Qualified JEE Advanced examination.
        - Certified in Hindi Prathamic examination by Dakshin Bharat Hindi Prachar Sabha
        - Consistent at receiving class position in Top 10.
        """)

        st.header("Memberships")
        st.write("""
        - Member of Computer Society of India.
        - Member of SheTek community.
        """)

        st.header("Hobbies")
        st.write("""
        - Spending time with family
        - Learning new things with trends
        - Humming music
        - Reading Moral story books
        - Listening to Moral stories
        """)

if __name__ == "__main__":
    main()
