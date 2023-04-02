import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

filename = 'model.pkl'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

def predict_price(year, km, mileage, engine, power, seats, price, loc_ah, loc_ban, loc_che, loc_coi, loc_del, loc_hyb, loc_jai, loc_koc, loc_kol, loc_mum, loc_pune, ft_cng, ft_die, ft_lpg, ft_pet, t_aut, t_man, ot_1, ot_45, ot_2, ot_3):
    input = np.array([[year, km, mileage, engine, power, seats, price, loc_ah, loc_ban, loc_che, loc_coi, loc_del, loc_hyb, loc_jai, loc_koc, loc_kol, loc_mum, loc_pune, ft_cng, ft_die, ft_lpg, ft_pet, t_aut, t_man, ot_1, ot_45, ot_2, ot_3]])
    prediction = loaded_model.predict(input)
    print(prediction)
    return prediction
