import streamlit as st
import time
import main_model
import plotly.express as px
import pandas as pd
import numpy as np

data_names = ["y", "a", "i", "g", "x", "b", "t", "m"]
if "data" not in st.session_state:
    st.session_state.data = {name: 0.0 for name in data_names}

# Sidebar inputs
inputs = st.sidebar.container()
with inputs:
    st.session_state.data["y"] = st.sidebar.number_input("Real national income (in G$)", step=5.0)
    st.session_state.data["a"] = st.sidebar.number_input("Autonomous consumption (in G$)", step=5.0)
    st.session_state.data["i"] = st.sidebar.number_input("Total investment (in G$)", step=5.0)
    st.session_state.data["g"] = st.sidebar.number_input("Autonomous gouv. purchases (in G$)", step=5.0)
    st.session_state.data["x"] = st.sidebar.number_input("Total exports (in G$)", step=5.0)
    st.session_state.data["b"] = st.sidebar.slider("Marginal propensity to consume", step=0.01, min_value=0.0, max_value=1.0)
    st.session_state.data["t"] = st.sidebar.slider("Tax rate", step=0.01, min_value=0.0, max_value=1.0)
    st.session_state.data["m"] = st.sidebar.slider("Marginal propensity to import", step=0.01, min_value=0.0, max_value=1.0)

# Streamlit settings
st.set_page_config(page_title="Simple short-run model", page_icon=":bar_chart:")
st.title("Simple short-run model\nECON209 - Midterm 1")
st.sidebar.header("Data inputs")

# Initialize session state for results
if "agg_exp" not in st.session_state:
    st.session_state.agg_exp = 0.0
    st.session_state.auto_exp = 0.0
    st.session_state.ind_exp = 0.0
if "delta" not in st.session_state:
    st.session_state.delta = 0.0

ph_ae_num = st.empty()
ph_data_change = st.empty()

# Function to render metrics with delta
def render_metric(curr_agg, prev_agg, curr_data, prev_data):
    st.session_state.delta = None if prev_agg is None else round(curr_agg -
                                                                 prev_agg, 2)
    ph_ae_num.metric("Aggregate Expenditure", curr_agg,
                     delta=st.session_state.delta,
                     delta_color="normal")

# Buttons for calculation and reset
calc, reset = st.sidebar.columns(2)
with calc:
    calculate_button = st.button("Calculate")
with reset:
    reset_button = st.button("Reset")

# Default values for previous data
prev_agg_exp = None

# Calculate logic
if calculate_button:
    prev_agg_exp = st.session_state.agg_exp
    prev_auto_exp = st.session_state.auto_exp
    prev_ind_exp = st.session_state.ind_exp
    prev_data_set = st.session_state.data.copy()

    # Call model function to get the new values
    new_agg_exp, new_auto_exp, new_ind_exp = main_model.calculate_ae(st.session_state.data)

    # Animate: 10 steps over ~0.4s
    steps = 10
    for i in range(1, steps + 1):
        interpolated = round(prev_agg_exp + (new_agg_exp - prev_agg_exp) * (i / steps), 2)
        render_metric(interpolated, prev_agg_exp, st.session_state.data, prev_data_set)
        time.sleep(0.04)

    st.session_state.agg_exp = new_agg_exp
    render_metric(st.session_state.agg_exp, prev_agg_exp, st.session_state.data, prev_data_set)
else:
    render_metric(st.session_state.agg_exp, None, None, None)
