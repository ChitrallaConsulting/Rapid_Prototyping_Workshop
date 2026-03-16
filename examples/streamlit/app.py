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

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Cormorant Garamond', serif; }
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
section[data-testid="stSidebar"] label { color: #f5ede0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
PLOT_BG  = "#1a1010"
PAPER_BG = "#1a1010"
FONT_CLR = "#c4a882"
GRID_CLR = "#3d2626"
LEGEND   = dict(bgcolor="#2d1b1b", bordercolor=GRID_CLR, borderwidth=1, font=dict(color="#f5ede0"))

def chart_title(text):
    return st.markdown(
        f"<h3 style='color:#2d1b1b; font-size:1.3rem; font-weight:600; letter-spacing:0.01em'>{text}</h3>",
        unsafe_allow_html=True,
    )

def base_layout(**kwargs):
    layout = dict(
        plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER_BG,
        font_color=FONT_CLR,
    )
    layout["margin"] = kwargs.pop("margin", dict(t=10, b=10))
    layout.update(kwargs)
    return layout

def empty_state():
    st.info("No data matches the current filters.")

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/alsace_wines.csv")
    df.columns = df.columns.str.strip()
    df["organic"] = df["organic"].str.strip()
    df["vintage_num"] = pd.to_numeric(df["vintage"], errors="coerce")
    df["vintage"] = df["vintage"].astype(str)
    df["value_index"] = (df["rating"] / df["price_eur"]).round(3)
    return df

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🍷 Filters")

    selected_grapes = st.multiselect(
        "Grape Variety", options=sorted(df["grape_variety"].unique()),
        default=sorted(df["grape_variety"].unique()),
    )
    selected_villages = st.multiselect(
        "Village", options=sorted(df["village"].unique()),
        default=sorted(df["village"].unique()),
    )
    selected_producers = st.multiselect(
        "Producer", options=sorted(df["producer"].unique()),
        default=sorted(df["producer"].unique()),
    )
    selected_classifications = st.multiselect(
        "Classification", options=sorted(df["classification"].unique()),
        default=sorted(df["classification"].unique()),
    )
    price_range = st.slider(
        "Price Range (€)",
        min_value=float(df["price_eur"].min()),
        max_value=float(df["price_eur"].max()),
        value=(float(df["price_eur"].min()), float(df["price_eur"].max())),
        step=0.5,
    )
    organic_filter = st.radio("Organic", options=["All", "Yes", "No"], horizontal=True)

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

n = len(filtered)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    "<h1 style='font-size:3.2rem; color:#2d1b1b; font-weight:600; margin-bottom:0; letter-spacing:-0.5px'>Alsace Wine Explorer</h1>"
    "<p style='color:#9e7c5a; font-size:1rem; margin-top:0; margin-bottom:2rem; font-family:DM Sans'>"
    "Explore, filter, and compare Alsace wines by variety, village, producer, and vintage."
    "</p>",
    unsafe_allow_html=True,
)

# ── Key metrics ───────────────────────────────────────────────────────────────
organic_pct = f"{(filtered['organic']=='Yes').sum() / n * 100:.0f}%" if n else "—"
best_value  = filtered.loc[filtered["value_index"].idxmax(), "grape_variety"] if n else "—"

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Wines",      n)
col2.metric("Avg. Rating",      f"{filtered['rating'].mean():.2f}"    if n else "—")
col3.metric("Avg. Price (€)",   f"{filtered['price_eur'].mean():.2f}" if n else "—")
col4.metric("Organic Share",    organic_pct)
col5.metric("Best Value Grape", best_value)

st.markdown("<hr style='border-color:#3d2626; margin:1.5rem 0'>", unsafe_allow_html=True)

# ── Row 1: Price distribution + Sunburst ─────────────────────────────────────
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    chart_title("Price Distribution by Grape Variety")
    if n:
        fig1 = px.box(
            filtered, x="grape_variety", y="price_eur",
            color="grape_variety", points="outliers",
            labels={"grape_variety": "Grape Variety", "price_eur": "Price (€)"},
        )
        fig1.update_layout(
            **base_layout(showlegend=False),
            xaxis=dict(showgrid=False, tickangle=-30),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR),
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        empty_state()

with chart_col2:
    chart_title("Classification Hierarchy")
    if n:
        fig2 = px.sunburst(
            filtered,
            path=["classification", "grape_variety", "producer"],
            color="grape_variety",
            labels={"classification": "Classification", "grape_variety": "Grape", "producer": "Producer"},
        )
        fig2.update_traces(textfont=dict(color="#f5ede0"))
        fig2.update_layout(**base_layout(height=420, margin=dict(t=10, b=10, l=10, r=10)))
        st.plotly_chart(fig2, use_container_width=True)
    else:
        empty_state()

# ── Row 2: Value Index + Vintage lines ───────────────────────────────────────
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    chart_title("Value Index  ·  Rating ÷ Price")
    if n:
        fig3 = px.scatter(
            filtered, x="price_eur", y="rating",
            color="grape_variety", size="value_index",
            hover_data=["producer", "village", "vintage", "value_index"],
            labels={"price_eur": "Price (€)", "rating": "Rating",
                    "grape_variety": "Grape", "value_index": "Value Index"},
            opacity=0.85,
        )
        top5 = filtered.nlargest(5, "value_index")
        fig3.add_traces(
            px.scatter(top5, x="price_eur", y="rating", hover_data=["producer", "value_index"])
            .update_traces(marker=dict(size=14, symbol="star",
                                       color="#ffd700", line=dict(width=1, color="#fff")))
            .data
        )
        fig3.update_layout(
            **base_layout(),
            xaxis=dict(showgrid=True, gridcolor=GRID_CLR),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR),
            legend=LEGEND,
        )
        st.plotly_chart(fig3, use_container_width=True)

        with st.expander("⭐ Top 5 Best-Value Wines"):
            st.dataframe(
                top5[["producer", "grape_variety", "vintage", "price_eur", "rating", "value_index"]]
                .sort_values("value_index", ascending=False).reset_index(drop=True),
                use_container_width=True,
            )
    else:
        empty_state()

with chart_col4:
    chart_title("Rating Across Vintages")
    if n:
        vintage_rating = (
            filtered.groupby(["vintage", "grape_variety"])["rating"]
            .mean().reset_index().sort_values("vintage")
        )
        y_min = max(0, vintage_rating["rating"].min() - 0.3)
        y_max = min(5, vintage_rating["rating"].max() + 0.3)
        fig4 = px.line(
            vintage_rating, x="vintage", y="rating",
            color="grape_variety", markers=True,
            labels={"vintage": "Vintage", "rating": "Avg Rating", "grape_variety": "Grape"},
            line_shape="spline",
        )
        fig4.update_traces(line=dict(width=2.5), marker=dict(size=7))
        fig4.update_layout(
            **base_layout(height=420, margin=dict(t=10, b=10, r=10)),
            xaxis=dict(showgrid=True, gridcolor=GRID_CLR,
                       tickmode="array", tickvals=sorted(vintage_rating["vintage"].unique())),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[y_min, y_max]),
            legend=LEGEND,
        )
        st.plotly_chart(fig4, use_container_width=True)
    else:
        empty_state()

# ── Row 3: Top producers + Avg rating by grape ───────────────────────────────
chart_col5, chart_col6 = st.columns([1, 2])

with chart_col5:
    chart_title("Top Producers by Avg Rating")
    if n:
        top_prod = (
            filtered.groupby("producer")["rating"]
            .agg(avg_rating="mean", wines="count")
            .query("wines >= 2")
            .sort_values("avg_rating", ascending=True)
            .tail(10).reset_index()
        )
        if top_prod.empty:
            st.caption("Need ≥ 2 wines per producer — try broadening filters.")
        else:
            fig5 = px.bar(
                top_prod, y="producer", x="avg_rating", orientation="h",
                color="avg_rating", color_continuous_scale="Reds",
                custom_data=["wines"],
                labels={"producer": "", "avg_rating": "Avg Rating"},
            )
            fig5.update_traces(
                hovertemplate="<b>%{y}</b><br>Avg Rating: %{x:.2f}<br>Wines: %{customdata[0]}<extra></extra>"
            )
            fig5.update_layout(
                **base_layout(coloraxis_showscale=False),
                xaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[0, 5]),
                yaxis=dict(showgrid=False),
            )
            st.plotly_chart(fig5, use_container_width=True)
    else:
        empty_state()

with chart_col6:
    chart_title("Avg Rating by Grape Variety")
    if n:
        rating_grape = (
            filtered.groupby("grape_variety")["rating"]
            .agg(avg_rating="mean", wines="count")
            .sort_values("avg_rating", ascending=False).reset_index()
        )
        fig6 = px.bar(
            rating_grape, x="grape_variety", y="avg_rating",
            color="avg_rating", color_continuous_scale="Reds",
            custom_data=["wines"],
            labels={"grape_variety": "Grape Variety", "avg_rating": "Avg Rating"},
        )
        fig6.update_traces(
            hovertemplate="<b>%{x}</b><br>Avg Rating: %{y:.2f}<br>Wines: %{customdata[0]}<extra></extra>"
        )
        fig6.update_layout(
            **base_layout(coloraxis_showscale=False),
            xaxis=dict(showgrid=False, tickangle=-30),
            yaxis=dict(showgrid=True, gridcolor=GRID_CLR, range=[0, 5]),
        )
        st.plotly_chart(fig6, use_container_width=True)
    else:
        empty_state()

# ── Data table ────────────────────────────────────────────────────────────────
st.markdown("<hr style='border-color:#3d2626; margin:1.5rem 0'>", unsafe_allow_html=True)
st.markdown(
    f"<h3 style='color:#2d1b1b; font-size:1.3rem; font-weight:600'>Filtered Data "
    f"<span style='font-size:1rem; color:#9e7c5a; font-family:DM Sans'>({n} wines)</span></h3>",
    unsafe_allow_html=True,
)

display_cols = ["wine_id", "grape_variety", "village", "producer",
                "classification", "vintage", "price_eur", "rating", "value_index", "organic"]

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
        "value_index":    st.column_config.NumberColumn("Value Index", format="%.3f",
                                                         help="Rating ÷ Price — higher = better value"),
        "organic":        st.column_config.TextColumn("Organic", width="small"),
    },
)

csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download filtered data as CSV",
    data=csv_data,
    file_name="alsace_wines_filtered.csv",
    mime="text/csv",
)
