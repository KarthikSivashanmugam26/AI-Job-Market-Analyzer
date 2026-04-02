import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="AI Job Market Analyzer", layout="wide")

st.title("🤖 AI Job Market Analyzer")

# Load dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "jobs.csv")
df = pd.read_csv(data_path)

# ---------------------------
# Dataset Preview
# ---------------------------

st.subheader("Dataset Preview")

st.dataframe(df)

# ---------------------------
# Metrics
# ---------------------------

st.subheader("Market Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", len(df))
col2.metric("Companies", df["company"].nunique())
col3.metric("Locations", df["location"].nunique())

# ---------------------------
# Top Companies
# ---------------------------

st.subheader("Top Hiring Companies")

company_counts = df["company"].value_counts()

colors = [
    "green" if v == company_counts.max()
    else "red" if v == company_counts.min()
    else "blue"
    for v in company_counts
]

fig = px.bar(
    x=company_counts.index,
    y=company_counts.values,
    labels={"x": "Company", "y": "Jobs"}
)

fig.update_traces(marker_color=colors)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Top Locations
# ---------------------------

st.subheader("Top Job Locations")

location_counts = df["location"].value_counts()

colors = [
    "green" if v == location_counts.max()
    else "red" if v == location_counts.min()
    else "blue"
    for v in location_counts
]

fig = px.bar(
    x=location_counts.index,
    y=location_counts.values,
    labels={"x": "Location", "y": "Jobs"}
)

fig.update_traces(marker_color=colors)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Skills Analysis
# ---------------------------

st.subheader("Top Skills Demand")

skills_series = df["skills"].str.split(",")
skills_series = skills_series.explode().str.strip()

skills_counts = skills_series.value_counts()

colors = [
    "green" if v == skills_counts.max()
    else "red" if v == skills_counts.min()
    else "blue"
    for v in skills_counts
]

fig = px.bar(
    x=skills_counts.index,
    y=skills_counts.values,
    labels={"x": "Skill", "y": "Demand"}
)

fig.update_traces(marker_color=colors)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Salary Distribution
# ---------------------------

st.subheader("Salary Distribution")

fig = px.histogram(df, x="salary")

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Experience Distribution
# ---------------------------

st.subheader("Experience Levels")

exp_counts = df["experience"].value_counts()

fig = px.pie(
    names=exp_counts.index,
    values=exp_counts.values
)

st.plotly_chart(fig, width="stretch")