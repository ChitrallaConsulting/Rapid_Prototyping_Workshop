"""
Rapid Prototyping Workshop — Streamlit Starter Template

This is a minimal starting point. Pick a dataset, uncomment the relevant
section, and start building. Use an LLM to help you add charts, filters,
and interactivity.

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ─── Page Config ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Data App Prototype",
    page_icon="⚡",
    layout="wide",
)

# ─── Title ───────────────────────────────────────────────────────────────────

st.title("⚡ Data App Prototype")
st.markdown("Built during the Rapid Prototyping Workshop")

# ─── Load Data ───────────────────────────────────────────────────────────────

# Uncomment ONE of the following lines to load a dataset:

# df = pd.read_csv("../../datasets/startup_funding.csv")
# df = pd.read_csv("../../datasets/coffee_survey.csv")
# df = pd.read_csv("../../datasets/city_bikes.csv")

# For demo purposes, we'll create a small sample dataframe:
df = pd.DataFrame({
    "category": ["A", "B", "C", "D", "E"],
    "value": [23, 45, 12, 67, 34],
    "growth": [1.2, 3.4, -0.5, 2.1, 0.8],
})

# ─── Sidebar Filters ────────────────────────────────────────────────────────

st.sidebar.header("Filters")
st.sidebar.markdown("Add your filters here using `st.sidebar` widgets.")

# Example filter (uncomment and adapt for your dataset):
# selected = st.sidebar.multiselect("Select categories", df["category"].unique())
# if selected:
#     df = df[df["category"].isin(selected)]

# ─── Metrics Row ─────────────────────────────────────────────────────────────

col1, col2, col3 = st.columns(3)
col1.metric("Total Rows", len(df))
col2.metric("Sum of Values", df["value"].sum())
col3.metric("Avg Growth", f"{df['growth'].mean():.1f}%")

# ─── Chart ───────────────────────────────────────────────────────────────────

st.subheader("Overview Chart")
fig = px.bar(df, x="category", y="value", color="category",
             title="Values by Category")
st.plotly_chart(fig, use_container_width=True)

# ─── Data Table ──────────────────────────────────────────────────────────────

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)

# ─── Next Steps ──────────────────────────────────────────────────────────────

st.markdown("---")
st.markdown("""
### Next Steps
1. **Load your dataset** — uncomment one of the `pd.read_csv` lines above
2. **Add filters** — use `st.sidebar.selectbox`, `st.slider`, `st.multiselect`
3. **Add charts** — use `plotly.express` for interactive visualizations
4. **Ask your LLM** — paste this code and ask it to add specific features

See the [Streamlit guide](../examples/streamlit/README.md) for step-by-step instructions.
""")
