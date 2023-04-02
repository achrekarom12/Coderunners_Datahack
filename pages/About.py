import streamlit as st
import requests


def run():

    with st.container():
        st.write("---")
        st.header("About us")
        st.subheader("""
        "None of us, ever do great things. But we can all do small things, with great love, and together we can do something wonderful."
        """)
        
        st.write("Our wonderful team:")
        mitali, om = st.columns(2)
        with mitali:
            st.subheader("Mitali Rawat")
            st.write("Email ID: mitali.201433201@vcet.edu.in")
            st.write("Contact: 8452813912")
            st.write("Vidyavardhini's College of Engineering & Technology, Vasai")

        with om:
            st.subheader("Om Achrekar")
            st.write("Email ID: om.201173105@vcet.edu.in")
            st.write("Contact: 9819930448")
            st.write("Vidyavardhini's College of Engineering & Technology, Vasai")


if __name__ == "__main__":
    run()
