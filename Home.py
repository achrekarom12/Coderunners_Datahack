import streamlit as st
import requests
# from streamlit_lottie import st_lottie
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)

# Useful links:
# https://www.webfx.com/tools/emoji-cheat-sheet/


def run():
    st.set_page_config(page_title="Car Resale Value Predictor",
                       page_icon=":computer:", layout="wide")

    # Header section
    with st.container():
        st.title("Car Resale Value Predictor")
        st.subheader(
            "A simple, minimalistic web app which will help you predict the resale value of your car.")

        st.write(
            "This simple, minimalistic web app is designed to help car owners predict the resale value of their vehicles. By inputting relevant details such as make, model, year of manufacture, mileage, condition, and photos of your car, the app uses machine learning algorithms to output a predicted resale value for the car. The app is built on a simple framework of Streamlit, with a clean and intuitive interface that allows users to quickly and easily get an estimated value for their vehicle. The accuracy of the app is based on data collected from various sources such as car sales websites, dealer listings, or auction sites, and the predictive model is continuously refined based on user feedback and additional data. Whether you are looking to sell your car in the near future or simply want to estimate the future resale value of your vehicle, this web app can help you make informed decisions and get the best value for your investment.")
    # slide 1
    with st.container():
        st.write("---")
        st.header("How to use the app")
        st.write("""
            To use the app, simply input the relevant details such as make, model, year of manufacture, mileage, condition, and photos of your car, and the app will use machine learning algorithms to output a predicted resale value for the car. The app is built on a simple framework of Streamlit, with a clean and intuitive interface that allows users to quickly and easily get an estimated value for their vehicle.
        """
        )
    

    # slide 2
    with st.container():
        st.write("---")
        st.header("Accuracy of the model")
        # st.write("##")
        st.write("""
            The accuracy of the model is based on data collected from various sources such as car sales websites, dealer listings, or auction sites, and the predictive model is continuously refined based on user feedback and additional data. Whether you are looking to sell your car in the near future or simply want to estimate the future resale value of your vehicle, this web app can help you make informed decisions and get the best value for your investment.
        """
        )

    # slide 3
    with st.container():
        st.write("---")
        st.header("Some Important Links")
        st.write("""
            - [GitHub Repo]("https://github.com/achrekarom12/Coderunners_Datahack")
            - [LinkedIn](https://www.linkedin.com/in/achrekarom)
            - [Text Dataset](https://drive.google.com/file/d/1MXEcWQ986cg6elbRNKcoiBmDoq8hxNR_/view)
            - [Image Dataset](https://data.mendeley.com/datasets/hj3vvx5946/1)

        """
        )


if __name__ == "__main__":
    run()
