import streamlit as st
import numpy as np
import pickle
with open("Iris_dataset.pkl" ,'rb' ) as f:
    model= pickle.load(f)

st.title("Iris Flower Prediction")
speal_length = st.slider("speal length(cm)" , 4.0 ,8.0)
speal_width = st.slider("speal width(cm)" , 2.0 ,5.0)
petal_length = st.slider("petal length(cm)" , 1.0 ,8.0)
petal_width = st.slider("petal width(cm)" , 0.1 ,3.0)

if st.button("Prediction"):
    input_data= np.array([[speal_length , speal_width, petal_length, petal_width]])
    prediction= model.predict(input_data)[0]
    species = [ 'Iris setosa', 'Iris versicolor', 'Iris virginica']
    st.success(f"Predicted Iris Species :{species[prediction]}")