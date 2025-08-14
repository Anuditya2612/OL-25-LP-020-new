import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Treatment Prediction:")

logi_reg_model=joblib.load("models/logistic_regression.pkl")

classification_models=joblib.load("models/classification_tasks.pkl")

rf_model=classification_models["Random Forest"]
svm_model=classification_models["SVM"]
xgb_model=classification_models["XGBoost"]