import streamlit as st
import Predictor
import pandas as pd
import cv2
import glob
import numpy as np
from keras import models
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from keras.preprocessing import image as image_utils
import keras.utils as image_utils
import os

CNN_Model = models.load_model("CNN_Car_detector.model")


def img_predictor(path):
    img = image_utils.load_img(path, target_size=(224, 224))
    img_array = image_utils.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)

    pred = CNN_Model.predict(img_batch)
    return pred


predict_price = Predictor.predict_price
# res = predict_price(2012, 61240, 22.48, 1995, 190, 5, 70.43, 0,
                    # 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0)


st.title("Get resale value for your car by answering just few question!")
# import streamlit as st

# Create a form using the form function
with st.form("My Form"):
    # Add a text input for the user's name
    st.subheader("Enter your car details")
    user = st.text_input("Name:")

    # Add a text input for the user's car model name
    car_name = st.text_input("Model:")

    # Add a number input for the user's year of purchase
    year = st.number_input("Year of Registeration:",
                           min_value=1999, max_value=2023)

  # Add a number input for the user's km
    km = st.number_input("Kilometers Driven:")

  # Add a number input for the user's mileage
    mileage = st.number_input("Mileage:")

  # Add a number input for the user's engine
    engine = st.number_input("Engine Capacity:")

  # Add a number input for the user's power
    power = st.number_input("Power:")

  # Add a number input for the user's price
    price = st.number_input("Purchase Price:")

    # Add a selectbox for the user's seats
    seats = st.selectbox("No. of seats:", options=[2, 3, 4, 5, 6, 7])

    # Add a selectbox for the user's location
    location = st.selectbox("Purchased from:", options=["Ahmedabad", "Bangalore", "Chennai",
                            "Coimbatore", "Delhi", "Hyderabad", "Jaipur", "Kochi", "Kolkata", "Mumbai", "Pune"])
    if (location == "Ahmedabad"):
        loc_ah = 1
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Bangalore"):
        loc_ah = 0
        loc_ban = 1
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Chennai"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 1
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Coimbatore"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 1
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Delhi"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 1
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Hyderabad"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 1
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Jaipur"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 1
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Kochi"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 1
        loc_kol = 0
        loc_mum = 0
        loc_pune = 0
    elif (location == "Kolkata"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 1
        loc_mum = 0
        loc_pune = 0
    elif (location == "Mumbai"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 1
        loc_pune = 0
    elif (location == "Pune"):
        loc_ah = 0
        loc_ban = 0
        loc_che = 0
        loc_coi = 0
        loc_del = 0
        loc_hyb = 0
        loc_jai = 0
        loc_koc = 0
        loc_kol = 0
        loc_mum = 0
        loc_pune = 1
    else:
        print("Invalid Location")

    # Add a selectbox for the user's fuel type
    fuel_type = st.selectbox("Fuel Type:", options=[
                             "CNG", "Diesel", "LPG", "Petrol"])
    if (fuel_type == "CNG"):
        ft_cng = 1
        ft_die = 0
        ft_lpg = 0
        ft_pet = 0
    elif (fuel_type == "Diesel"):
        ft_cng = 0
        ft_die = 1
        ft_lpg = 0
        ft_pet = 0
    elif (fuel_type == "LPG"):
        ft_cng = 0
        ft_die = 0
        ft_lpg = 1
        ft_pet = 0
    elif (fuel_type == "Petrol"):
        ft_cng = 0
        ft_die = 0
        ft_lpg = 0
        ft_pet = 1
    else:
        print("Invalid Fuel Type")

    # Add a selectbox for the user's transmission type
    transmission = st.selectbox("Transmission Type:", options=[
                                "Automatic", "Manual"])
    if (transmission == "Automatic"):
        t_aut = 1
        t_man = 0
    elif (transmission == "Manual"):
        t_aut = 0
        t_man = 1

    # Add a selectbox for the user's owner type
    owner_type = st.selectbox("Owner Type:", options=[
                              "First", "Fourth & Above", "Second", "Third"])
    if (owner_type == "First"):
        ot_1 = 1
        ot_45 = 0
        ot_2 = 0
        ot_3 = 0
    elif (owner_type == "Fourth & Above"):
        ot_1 = 0
        ot_45 = 1
        ot_2 = 0
        ot_3 = 0
    elif (owner_type == "Second"):
        ot_1 = 0
        ot_45 = 0
        ot_2 = 1
        ot_3 = 0
    elif (owner_type == "Third"):
        ot_1 = 0
        ot_45 = 0
        ot_2 = 0
        ot_3 = 1
    else:
        print("Invalid Owner Type")

    # Use the file uploader to upload an image
    image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

     # If an image is uploaded, display it
    if image is not None:
        # st.image(image, caption='Uploaded image', use_column_width=True)
        # state.image_path = image.name
        print("meow")


    # Add a checkbox fto let know whether this vehicle color is faded or not
    fading_color = st.checkbox("Do you want to check for fading color?")
    st.write("(You will have to upload an original image of your vehicle for this)")


    # Add a checkbox fto let know whether this vehicle has met with an accident or not
    accident = st.checkbox("Has your vehicle met with an accident?")
    
    # Add a submit button to the form
    submitted = st.form_submit_button("Submit")


# Display the user's input if the form was submitted
if submitted:
    res = predict_price(year, km, mileage, engine, power, seats, price, loc_ah, loc_ban, loc_che, loc_coi, loc_del, loc_hyb, loc_jai, loc_koc, loc_kol, loc_mum, loc_pune, ft_cng, ft_die, ft_lpg, ft_pet, t_aut, t_man, ot_1, ot_45, ot_2, ot_3)
    st.header("Welcome, " + user)
    st.write("---")
    st.write("Your Car:", car_name)
    st.write("Registered in", str(year))
    st.write("Driven", str(km), "Kilometers")
    # st.write("Predicted Price of your car is", str(res[0]), "Lakhs")


   
    val = img_predictor(image)

    # once the checkbox is checked, the price is reduced by 4%
    if accident:
        # price = float(str(res[0]))
        price = res[0]
        final_price = price - (price*0.2)
        final = round(final_price, 2)
        # st.write("Predicted Price of your car is", str(final), "Lakhs")
    else:
        # st.write("Predicted Price of your car is", str(res[0]), "Lakhs")
        final = res[0]

    # print("Car is not Damaged: "+str(pred[0][0])+", Car is Damaged: "+str(pred[0][1]))
    if val[0][0] > val[0][1]:
        st.subheader(
                "We see your car don't have any dents and scratches, so based on our analysis, resale value of your car will be,")
        price = final
        final = round(price, 2)
        # st.write("Predicted Price of your car is")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.subheader(str(final) + " Lakhs")

        with col3:
            st.write(' ')

    else:
        st.subheader(
                "We see your car do have dents and scratches, so based on our analysis, resale value of your car will be ,")
            # price = float(str(res[0]))
        price = final
        final_price = price - (price*0.3)
        final = round(final_price, 2)
        # st.subheader("Predicted Price of your car is")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.header(str(final) + " Lakhs")

        with col3:
            st.write(' ')

    if fading_color:
        st.subheader("Since your vehicle color have been faded, resale value of your car will be , ")
        # price = float(str(res[0]))
        price = final
        final_price = price - (price*0.2)
        final = round(final_price, 2)
        # st.subheader("Predicted Price of your car is")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.header(str(final) + " Lakhs")

        with col3:
            st.write(' ')
            
