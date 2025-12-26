import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Business 360 Dashboard", layout="wide")

st.title("Business 360 – Risk & Performance Dashboard")
st.caption("Built by Brahma Naidu | Business Analytics & AI")

st.sidebar.header("Upload business data (CSV)")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file is None:
    st.info("Upload a CSV file with columns: Date, Revenue, Cost")
    st.stop()

df = pd.read_csv(file)
df["Profit"] = df["Revenue"] - df["Cost"]

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
col2.metric("Total Cost", f"${df['Cost'].sum():,.0f}")
col3.metric("Total Profit", f"${df['Profit'].sum():,.0f}")

st.subheader("Monthly Performance")
fig = px.line(
    df,
    x="Date",
    y=["Revenue", "Cost", "Profit"],
    markers=True
)
st.plotly_chart(fig, width="stretch")
