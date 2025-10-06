import streamlit as st

import main_model

# a, i, g, x, b, t, m, y

st.title("Simple short-run model\nECON209 - Midterm 1")
st.sidebar.header("Data inputs")

y = st.sidebar.number_input("Real national income (in G$)", step=1)
a = st.sidebar.number_input("Autonomous consumption (in G$)", step=1)
i = st.sidebar.number_input("Total investment (in G$)", step=1)
g = st.sidebar.number_input("Autonomous gouv. purchases (in G$)", step=1)
x = st.sidebar.number_input("Total exports (in G$)", step=1)
b = st.sidebar.slider("Marginal propensity to consume", step=0.01,
                      min_value=0.0, max_value=1.0)
t = st.sidebar.slider("Taxe rate", step=0.01,
                      min_value=0.0, max_value=1.0)
m = st.sidebar.slider("Marginal propensity to import", step=0.01,
                      min_value=0.0, max_value=1.0)
ae = 0

calc, reset = st.sidebar.columns(2)
with calc:
    st.button("Calculate")
with reset:
    st.button("Reset")

if calc:
    ae, auto_ex, ind_ex = main_model.calculate_ae(a, i, g, x, b,t, m, y)
elif reset:
    ae = 0
else:
    ae = 0



st.metric(label="Aggregate expenditure", value=ae, delta="0.0%")
