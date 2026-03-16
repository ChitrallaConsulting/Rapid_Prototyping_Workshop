import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Alsace Wine Explorer",
    page_icon="🍷",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif;
}
.stMetric {
    background: linear-gradient(135deg, #2d1b1b 0%, #3d2626 100%);
    border: 1px solid #7a3e3e44;
    border-radius: 12px;
    padding: 16px 20px;
}
.stMetric label { color: #c4a882 !important; font-size: 0.75rem !important; letter-spacing: 0.1em; text-transform: uppercase; }
.stMetric [data-testid="stMetricValue"] { color: #f5ede0 !important; font-family: 'Cormorant Garamond', serif; font-size: 2rem !important; }
.block-container { padding-top: 2rem; }
section[data-testid="stSidebar"] { background-color: #1a1010; }
section[data-testid="stSidebar"] .stMarkdown h2 { color: #c4a882; font-family: 'Cormorant Garamond', serif; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/alsace_wines.csv")
    df.columns = df.columns.str.strip()
    df["vintage"] = df["vintage"].astype(str)
    df["organic"] = df["organic"].str.strip()
    return df

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍷 Filters")

    grape_options = sorted(df["grape_variety"].unique())
    selected_grapes = st.multiselect(
        "Grape Variety",
        options=grape_options,
        default=grape_options,
    )

    village_options = sorted(df["village"].unique())
    selected_villages = st.multiselect(
        "Village",
        options=village_options,
        default=village_options,
    )

    producer_options = sorted(df["producer"].unique())
    selected_producers = st.multiselect(
        "Producer",
        options=producer_options,
        default=producer_options,
    )

    classification_options = sorted(df["classification"].unique())
    selected_classifications = st.multiselect(
        "Classification",
        options=classification_options,
        default=classification_options,
    )

    price_min = float(df["price_eur"].min())
    price_max = float(df["price_eur"].max())
    price_range = st.slider(
        "Price Range (€)",
        min_value=price_min,
        max_value=price_max,
        value=(price_min, price_max),
        step=0.5,
    )

    organic_filter = st.radio(
        "Organic",
        options=["All", "Yes", "No"],
        horizontal=True,
    )

# ── Apply filters ─────────────────────────────────────────────────────────────
filtered = df[
    df["grape_variety"].isin(selected_grapes)
    & df["village"].isin(selected_villages)
    & df["producer"].isin(selected_producers)
    & df["classification"].isin(selected_classifications)
    & df["price_eur"].between(*price_range)
]
if organic_filter != "All":
    filtered = filtered[filtered["organic"] == organic_filter]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    "<h1 style='font-size:2.8rem; color:#f5ede0; margin-bottom:0'>Alsace Wine Explorer</h1>"
    "<p style='color:#9e7c5a; font-size:1rem; margin-top:0; margin-bottom:2rem; font-family:DM Sans'>"
    "Explore, filter, and compare Alsace wines by variety, village, producer, and vintage."
    "</p>",
    unsafe_allow_html=True,
)

# ── Key metrics ───────────────────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Wines", len(filtered))
col2.metric("Avg. Rating", f"{filtered['rating'].mean():.2f}" if len(filtered) else "—")
col3.metric("Avg. Price (€)", f"{filtered['price_eur'].mean():.2f}" if len(filtered) else "—")
col4.metric("Grape Varieties", filtered["grape_variety"].nunique())
col5.metric("Organic", f"{(filtered['organic']=='Yes').sum()} wines")

st.markdown("<hr style='border-color:#3d2626; margin:1.5rem 0'>", unsafe_allow_html=True)

# ── Charts ────────────────────────────────────────────────────────────────────
PLOT_BG   = "#1a1010"
PAPER_BG  = "#1a1010"
FONT_CLR  = "#c4a882"
GRID_CLR  = "#3d2626"
PALETTE   = px.colors.sequential.Reds_r

chart_col1, chart_col2 = st.columns(2)

# 1. Avg Rating by Grape Variety (bar)
with chart_col1:
    st.markdown("<h3 style='color:#f5ede0'>Avg Rating by Grape Variety</h3>", unsafe_allow_html=True)
    if not filtered.empty:
        rating_grape = (
            filtered.groupby("grape_variety")["rating"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )
        fig1 = px.bar(
            rating_grape, x="grape_variety", y="rating",
            color="rating", color_continuous_scale="Reds",
            labels={"grape_variety": "Grape Variety", "rating": "Avg Rating"},
        )
        fig1.update_layout(
            plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG,
            font_color=FONT_CLR, coloraxis_showscale=False,
            xaxis=dict(showgrid=False, tickangle=-30),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[0, 5]),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No data for current filters.")

# 2. Price vs Rating scatter
with chart_col2:
    st.markdown("<h3 style='color:#f5ede0'>Price vs Rating</h3>", unsafe_allow_html=True)
    if not filtered.empty:
        fig2 = px.scatter(
            filtered, x="price_eur", y="rating",
            color="grape_variety", hover_data=["producer", "village", "vintage"],
            labels={"price_eur": "Price (€)", "rating": "Rating", "grape_variety": "Grape"},
            opacity=0.85, size_max=10,
        )
        fig2.update_traces(marker=dict(size=8))
        fig2.update_layout(
            plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG,
            font_color=FONT_CLR,
            xaxis=dict(showgrid=True, gridcolor=GRID_CLR),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR),
            legend=dict(bgcolor="#2d1b1b", bordercolor=GRID_CLR, borderwidth=1, font=dict(color="#f5ede0")),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No data for current filters.")

chart_col3, chart_col4 = st.columns(2)

# 3. Avg Rating by Vintage (line)
with chart_col3:
    st.markdown("<h3 style='color:#f5ede0'>Rating Across Vintages</h3>", unsafe_allow_html=True)
    if not filtered.empty:
        vintage_rating = (
            filtered.groupby(["vintage", "grape_variety"])["rating"]
            .mean()
            .reset_index()
            .sort_values("vintage")
        )
        fig3 = px.line(
            vintage_rating, x="vintage", y="rating",
            color="grape_variety", markers=True,
            labels={"vintage": "Vintage", "rating": "Avg Rating", "grape_variety": "Grape"},
        )
        fig3.update_layout(
            plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG,
            font_color=FONT_CLR,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[0, 5]),
            legend=dict(bgcolor="#2d1b1b", bordercolor=GRID_CLR, borderwidth=1, font=dict(color="#f5ede0")),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No data for current filters.")

# 4. Top Producers by Avg Rating (horizontal bar)
with chart_col4:
    st.markdown("<h3 style='color:#f5ede0'>Top Producers by Avg Rating</h3>", unsafe_allow_html=True)
    if not filtered.empty:
        top_producers = (
            filtered.groupby("producer")["rating"]
            .agg(avg_rating="mean", count="count")
            .query("count >= 1")
            .sort_values("avg_rating", ascending=True)
            .tail(10)
            .reset_index()
        )
        fig4 = px.bar(
            top_producers, y="producer", x="avg_rating",
            orientation="h", color="avg_rating", color_continuous_scale="Reds",
            labels={"producer": "", "avg_rating": "Avg Rating"},
        )
        fig4.update_layout(
            plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG,
            font_color=FONT_CLR, coloraxis_showscale=False,
            xaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[0, 5]),
            yaxis=dict(showgrid=False),
            margin=dict(t=10, b=10),
        )
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No data for current filters.")

# ── Data table ────────────────────────────────────────────────────────────────
st.markdown("<hr style='border-color:#3d2626; margin:1.5rem 0'>", unsafe_allow_html=True)
st.markdown(
    f"<h3 style='color:#f5ede0'>Filtered Data "
    f"<span style='font-size:1rem; color:#9e7c5a; font-family:DM Sans'>({len(filtered)} wines)</span></h3>",
    unsafe_allow_html=True,
)

display_cols = ["wine_id", "grape_variety", "village", "producer",
                "classification", "vintage", "price_eur", "rating", "organic"]

st.dataframe(
    filtered[display_cols].sort_values("rating", ascending=False).reset_index(drop=True),
    use_container_width=True,
    height=400,
    column_config={
        "wine_id":        st.column_config.NumberColumn("ID", width="small"),
        "grape_variety":  st.column_config.TextColumn("Grape"),
        "village":        st.column_config.TextColumn("Village"),
        "producer":       st.column_config.TextColumn("Producer"),
        "classification": st.column_config.TextColumn("Classification"),
        "vintage":        st.column_config.TextColumn("Vintage", width="small"),
        "price_eur":      st.column_config.NumberColumn("Price (€)", format="€%.2f"),
        "rating":         st.column_config.ProgressColumn("Rating", min_value=0, max_value=5, format="%.1f"),
        "organic":        st.column_config.TextColumn("Organic", width="small"),
    },
)

# ── Download ──────────────────────────────────────────────────────────────────
csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download filtered data as CSV",
    data=csv_data,
    file_name="alsace_wines_filtered.csv",
    mime="text/csv",
)
