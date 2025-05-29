import streamlit as st
import pandas as pd
import numpy as np

st.title("Sample BI Dashboard")
data = pd.DataFrame(np.random.randn(10, 3), columns=["Metric A", "Metric B", "Metric C"])
st.line_chart(data)