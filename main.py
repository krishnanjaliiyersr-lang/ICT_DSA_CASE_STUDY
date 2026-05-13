
# Libraries
import pickle
import streamlit as st
import numpy as np

st.title('web app')
with open('model.pkl','rb') as f:
          lr_model= pickle.load(f)
sl=st.slider('Insert a sepel length',0, 10, 1)
sw=st.slider('Insert a sepel width', 0,10, 1)
pl=st.slider('Insert a petal length',0, 10,1)
pw=st.slider('Insert a petal width',0,10,1)


if st.button('predict'):
    pred=lr_model.predict(np.array([[sl,sw,pl,pw]]))
    st.write('The flower is:', pred[0])
# pip install stream numpy scikit-learn
# python -m stream run main.py
