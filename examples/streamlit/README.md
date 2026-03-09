# Streamlit Step-by-Step Guide

A complete guide to building your data app prototype with Streamlit during the workshop.

## What is Streamlit?

Streamlit is a Python framework that turns scripts into interactive web apps. You write Python — Streamlit handles the UI. No HTML, CSS, or JavaScript needed.

## Quick Start

```bash
# From the repo root
pip install -r examples/streamlit/requirements.txt
streamlit run examples/streamlit/app.py
```

Your app opens at `http://localhost:8501`.

## Step 1: Load Your Dataset

Replace the sample data in `app.py` with your chosen dataset:

```python
import pandas as pd

df = pd.read_csv("../../datasets/startup_funding.csv")

# Quick check
st.write(f"Loaded {len(df)} rows and {len(df.columns)} columns")
st.dataframe(df.head())
```

## Step 2: Add Sidebar Filters

Filters let users explore the data interactively:

```python
st.sidebar.header("Filters")

# Dropdown filter
industry = st.sidebar.selectbox("Industry", ["All"] + sorted(df["industry"].unique()))
if industry != "All":
    df = df[df["industry"] == industry]

# Multi-select filter
stages = st.sidebar.multiselect("Funding Stage", df["funding_stage"].unique())
if stages:
    df = df[df["funding_stage"].isin(stages)]

# Range slider
min_val, max_val = int(df["amount_usd"].min()), int(df["amount_usd"].max())
amount_range = st.sidebar.slider("Funding Amount", min_val, max_val, (min_val, max_val))
df = df[df["amount_usd"].between(*amount_range)]
```

## Step 3: Add Metrics

Show key numbers at a glance:

```python
col1, col2, col3 = st.columns(3)
col1.metric("Total Companies", len(df))
col2.metric("Total Funding", f"${df['amount_usd'].sum():,.0f}")
col3.metric("Avg Round Size", f"${df['amount_usd'].mean():,.0f}")
```

## Step 4: Add Charts

Use Plotly for interactive visualizations:

```python
import plotly.express as px

# Bar chart
fig = px.bar(df, x="industry", y="amount_usd", color="funding_stage",
             title="Funding by Industry and Stage")
st.plotly_chart(fig, use_container_width=True)

# Scatter plot
fig2 = px.scatter(df, x="date", y="amount_usd", color="industry",
                  size="amount_usd", hover_name="company_name",
                  title="Funding Timeline")
st.plotly_chart(fig2, use_container_width=True)

# Pie chart
fig3 = px.pie(df, names="funding_stage", values="amount_usd",
              title="Funding Distribution by Stage")
st.plotly_chart(fig3, use_container_width=True)
```

## Step 5: Add Interactivity

```python
# Tabs for different views
tab1, tab2 = st.tabs(["Charts", "Raw Data"])

with tab1:
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.dataframe(df, use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False), "filtered_data.csv")
```

## Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repo
4. Select `examples/streamlit/app.py` as the main file
5. Click **Deploy**

Your app is now live with a shareable URL.

## Useful Streamlit Components

| Component | Use For | Example |
|-----------|---------|---------|
| `st.selectbox` | Single selection dropdown | Filter by category |
| `st.multiselect` | Multiple selections | Filter by multiple tags |
| `st.slider` | Numeric range | Filter by amount/date |
| `st.columns` | Side-by-side layout | Metrics row |
| `st.tabs` | Tabbed content | Charts vs. data table |
| `st.metric` | KPI display | Total, average, count |
| `st.plotly_chart` | Interactive charts | Bar, scatter, pie |
| `st.dataframe` | Interactive table | Browse raw data |
| `st.download_button` | Export data | Download filtered CSV |

## LLM Prompts for Streamlit

Copy-paste these to your LLM for quick help:

**Add a filter:**
> "I have a Streamlit app with a pandas DataFrame `df` that has columns [list your columns]. Add a sidebar filter for the [column name] column."

**Add a chart:**
> "Add a Plotly bar chart to my Streamlit app showing [metric] by [category]. The DataFrame has these columns: [list columns]."

**Fix a bug:**
> "I'm getting this error in my Streamlit app: [paste error]. Here's my code: [paste code]. How do I fix it?"

## Reference

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Plotly Express](https://plotly.com/python/plotly-express/)
