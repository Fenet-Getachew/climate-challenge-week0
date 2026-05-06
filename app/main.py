import streamlit as st
import plotly.express as px
from utils import load_all_data

# Page Config
st.set_page_config(page_title="COP32 Climate Vulnerability Portal", layout="wide")

st.title("🌍 African Climate Vulnerability Dashboard")
st.markdown("### Data-driven insights for Ethiopia's COP32 Position Paper (2015-2026)")

# Load Data
try:
    df = load_all_data()
except Exception as e:
    st.error(f"Please ensure cleaned CSVs are in the 'data/' folder. Error: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")

# 1. Country Selector
selected_countries = st.sidebar.multiselect(
    "Select Countries:",
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

# 2. Year Range Slider
min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
selected_years = st.sidebar.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# 3. Variable Selector
variable_map = {
    "Temperature (°C)": "T2M",
    "Precipitation (mm/day)": "PRECTOTCORR",
    "Relative Humidity (%)": "RH2M",
    "Wind Speed (m/s)": "WS2M"
}
selected_label = st.sidebar.selectbox("Select Climate Variable:", options=list(variable_map.keys()))
selected_var = variable_map[selected_label]

# --- DATA FILTERING LOGIC ---
filtered_df = df[
    (df['Country'].isin(selected_countries)) & 
    (df['Year'] >= selected_years[0]) & 
    (df['Year'] <= selected_years[1])
]

# --- DASHBOARD VISUALS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{selected_label} Trends Over Time")
    fig_line = px.line(
        filtered_df, 
        x='Date', 
        y=selected_var, 
        color='Country',
        template="plotly_white",
        labels={selected_var: selected_label}
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader(f"{selected_label} Distribution by Country")
    fig_box = px.box(
        filtered_df, 
        x='Country', 
        y=selected_var, 
        color='Country',
        template="plotly_white",
        labels={selected_var: selected_label}
    )
    st.plotly_chart(fig_box, use_container_width=True)

# --- KEY METRICS SUMMARY ---
st.divider()
st.subheader("Summary Statistics for Selected Period")
stats_df = filtered_df.groupby('Country')[selected_var].agg(['mean', 'max', 'std']).reset_index()
st.table(stats_df.style.format(precision=2))